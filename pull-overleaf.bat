@echo off
echo Obteniendo cambios desde Overleaf...
git fetch overleaf

echo Fusionando cambios...
git merge overleaf/master --no-commit --no-ff 2>nul

REM Restaurar archivos de configuración que no deben eliminarse
echo Restaurando archivos de configuración...
git checkout HEAD -- README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>nul

REM Restaurar carpeta PRUEBAS (proyecto Lean4, no viene de Overleaf)
git checkout HEAD -- PRUEBAS 2>nul

REM Restaurar carpeta TFG_GABRIEL (no viene de Overleaf)
git checkout HEAD -- TFG_GABRIEL 2>nul

REM Eliminar carpeta que solo debe estar en Overleaf
git rm -rf "Artículos Base" 2>nul

REM Completar el merge
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo No hay cambios nuevos desde Overleaf
    git merge --abort 2>nul
) else (
    git commit -m "Merge cambios desde Overleaf"
    echo.
    echo ¡Sincronización completa!
    echo Cambios desde Overleaf aplicados correctamente
)
