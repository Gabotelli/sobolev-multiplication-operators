@echo off
echo Subiendo a GitHub...
git push origin master
if %errorlevel% neq 0 (
    echo Error al subir a GitHub
    exit /b %errorlevel%
)

echo.
echo Preparando push a Overleaf (3 carpetas limpias)...
git fetch overleaf

git branch -D overleaf-sync 2>nul
git checkout -b overleaf-sync master

REM Traer la carpeta desde Overleaf para que no se borre en el push
git checkout overleaf/master -- "Artículos Base" 2>nul

REM Eliminar archivos de configuracion de la raiz
git rm -f README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>nul

REM Eliminar carpetas que no deben ir a Overleaf
git rm -rf PRUEBAS 2>nul
git rm -rf "TFG_GABRIEL" 2>nul

REM Eliminar archivos de compilacion LaTeX de las 3 carpetas principales
echo Eliminando archivos de compilacion...
for %%D in ("Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES") do (
    if exist "%%~D" (
        for /r "%%~D" %%F in (*.aux *.log *.out *.toc *.synctex.gz *.bbl *.blg *.bcf *.run.xml *.fls *.fdb_latexmk *.idx *.ind *.ilg *.bak *.pdf) do (
            git rm -f "%%F" 2>nul
        )
    )
)

REM Commit los cambios
git commit -m "Sync to Overleaf: remove config files and compilation artifacts" --no-verify 2>nul

REM Push a Overleaf
echo Subiendo a Overleaf...
git push overleaf overleaf-sync:master

REM Si falla, intentar con pull y merge
if %errorlevel% neq 0 (
    echo Sincronizando con Overleaf...
    git pull overleaf master --no-edit --strategy-option theirs 2>nul
    
    REM Re-aplicar eliminaciones
    git rm -f README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>nul
    git rm -rf PRUEBAS 2>nul
    git rm -rf "TFG_GABRIEL" 2>nul
    
    for %%D in ("Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES") do (
        if exist "%%~D" (
            for /r "%%~D" %%F in (*.aux *.log *.out *.toc *.synctex.gz *.bbl *.blg *.bcf *.run.xml *.fls *.fdb_latexmk *.idx *.ind *.ilg *.bak *.pdf) do (
                git rm -f "%%F" 2>nul
            )
        )
    )
    
    REM Restaurar archivos desde master
    git checkout master -- "Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES" 2>nul
    
    REM Volver a limpiar
    for %%D in ("Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES") do (
        if exist "%%~D" (
            for /r "%%~D" %%F in (*.aux *.log *.out *.toc *.synctex.gz *.bbl *.blg *.bcf *.run.xml *.fls *.fdb_latexmk *.idx *.ind *.ilg *.bak *.pdf) do (
                git rm -f "%%F" 2>nul
            )
        )
    )
    
    REM Recuperar "Artículos Base" desde el servidor de Overleaf
    git checkout overleaf/master -- "Artículos Base" 2>nul
    
    git commit -m "Remove config and build artifacts after merge" --no-verify 2>nul
    git push overleaf overleaf-sync:master
)

REM Volver a master
git checkout master
git branch -D overleaf-sync

echo.
echo ¡Sincronizacion completa!
echo - GitHub: con README, .gitignore y scripts
echo - Overleaf: Plantilla TFM, Notas para trabajar, RESUMEN DE REUNIONES (sin basura de compilacion)
