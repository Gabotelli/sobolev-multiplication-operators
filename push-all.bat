@echo off
echo Subiendo a GitHub...
git push origin master
if %errorlevel% neq 0 (
    echo Error al subir a GitHub
    exit /b %errorlevel%
)

echo.
echo Preparando push a Overleaf (solo carpetas de trabajo)...

REM Fetch desde Overleaf
git fetch overleaf

REM Crear branch temporal desde master
git branch -D overleaf-sync 2>nul
git checkout -b overleaf-sync master

REM Traer la carpeta desde Overleaf para que no se borre en el push
git checkout overleaf/master -- "Artículos Base" 2>nul

REM Eliminar archivos de configuración
git rm -f README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>nul

REM Eliminar carpeta PRUEBAS (no debe ir a Overleaf)
git rm -rf PRUEBAS 2>nul

REM Eliminar carpeta TFG_GABRIEL (no debe ir a Overleaf)
git rm -rf "TFG_GABRIEL" 2>nul

REM Eliminar archivos que no sean .tex ni .bib de "Notas para trabajar" y "RESUMEN DE REUNIONES"
echo Filtrando archivos para Overleaf...
for /r "Notas para trabajar" %%F in (*) do if not "%%~xF"==".tex" if not "%%~xF"==".bib" git rm -f "%%F" 2>nul
for /r "RESUMEN DE REUNIONES" %%F in (*) do if not "%%~xF"==".tex" if not "%%~xF"==".bib" git rm -f "%%F" 2>nul

REM Commit los cambios
git commit -m "Remove config files and non-tex files for Overleaf sync" --no-verify 2>nul

REM Push a Overleaf
echo Subiendo a Overleaf...
git push overleaf overleaf-sync:master

REM Si falla, intentar con pull y merge
if %errorlevel% neq 0 (
    echo Sincronizando con Overleaf...
    git pull overleaf master --no-edit --strategy-option theirs 2>nul
    REM Asegurarse de que los archivos sigan eliminados
    git rm -f README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>nul
    git rm -rf PRUEBAS 2>nul
    git rm -rf "TFG_GABRIEL" 2>nul
    for /r "Notas para trabajar" %%F in (*) do if not "%%~xF"==".tex" if not "%%~xF"==".bib" git rm -f "%%F" 2>nul
    for /r "RESUMEN DE REUNIONES" %%F in (*) do if not "%%~xF"==".tex" if not "%%~xF"==".bib" git rm -f "%%F" 2>nul
    REM Restaurar archivos .tex y .bib desde master si fueron eliminados
    git checkout master -- "Notas para trabajar/*.tex" "Notas para trabajar/*.bib" 2>nul
    git checkout master -- "RESUMEN DE REUNIONES/*.tex" "RESUMEN DE REUNIONES/*.bib" 2>nul
    REM Recuperar "Artículos Base" desde el servidor de Overleaf para que no se borre
    git checkout overleaf/master -- "Artículos Base" 2>nul
    git commit -m "Remove config files and non-tex files after merge" --no-verify 2>nul
    git push overleaf overleaf-sync:master
)

REM Volver a master
git checkout master
git branch -D overleaf-sync

echo.
echo ¡Sincronización completa!
echo - GitHub: con README, .gitignore y scripts
echo - Overleaf: solo carpetas de trabajo
