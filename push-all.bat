@echo off
echo Subiendo a GitHub...
git push origin master
if %errorlevel% neq 0 (
    echo Error al subir a GitHub
    exit /b %errorlevel%
)

echo.
echo Preparando push a Overleaf (solo carpetas de trabajo)...

REM Crear branch temporal para Overleaf
git branch -D overleaf-sync 2>nul
git checkout -b overleaf-sync

REM Eliminar README y .gitignore solo de este branch
git rm --cached README.md .gitignore
git commit -m "Remove config files for Overleaf sync" --no-verify

REM Hacer push a Overleaf
echo Subiendo a Overleaf...
git push overleaf overleaf-sync:master --force

REM Volver a master
git checkout master
git branch -D overleaf-sync

echo.
echo ¡Sincronización completa!
echo - GitHub: con README y .gitignore
echo - Overleaf: solo carpetas de trabajo
