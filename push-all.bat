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

REM Eliminar archivos de configuración
git rm -f README.md .gitignore push-all.bat push-all.sh 2>nul

REM Commit los cambios
git commit -m "Remove config files for Overleaf sync" --no-verify 2>nul

REM Push a Overleaf
echo Subiendo a Overleaf...
git push overleaf overleaf-sync:master

REM Si falla, intentar con pull y merge
if %errorlevel% neq 0 (
    echo Sincronizando con Overleaf...
    git pull overleaf master --no-edit --strategy-option theirs 2>nul
    REM Asegurarse de que los archivos sigan eliminados
    git rm -f README.md .gitignore push-all.bat push-all.sh 2>nul
    git commit -m "Remove config files after merge" --no-verify 2>nul
    git push overleaf overleaf-sync:master
)

REM Volver a master
git checkout master
git branch -D overleaf-sync

echo.
echo ¡Sincronización completa!
echo - GitHub: con README, .gitignore y scripts
echo - Overleaf: solo carpetas de trabajo
