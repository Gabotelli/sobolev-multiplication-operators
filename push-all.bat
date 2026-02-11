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

REM Crear branch temporal basado en Overleaf
git branch -D overleaf-sync 2>nul
git checkout -b overleaf-sync overleaf/master

REM Eliminar archivos de configuración si existen
if exist README.md git rm README.md
if exist .gitignore git rm .gitignore
if exist push-all.bat git rm push-all.bat
if exist push-all.sh git rm push-all.sh

REM Commit solo si hay cambios
git diff --cached --quiet
if %errorlevel% neq 0 (
    git commit -m "Remove config files for Overleaf sync" --no-verify
)

REM Merge con master
git merge master --no-edit -X theirs

REM Push a Overleaf
echo Subiendo a Overleaf...
git push overleaf overleaf-sync:master

REM Volver a master
git checkout master
git branch -D overleaf-sync

echo.
echo ¡Sincronización completa!
echo - GitHub: con README, .gitignore y scripts
echo - Overleaf: solo carpetas de trabajo
