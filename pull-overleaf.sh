#!/bin/bash

echo "Obteniendo cambios desde Overleaf..."
git fetch overleaf

echo "Fusionando cambios..."
git merge overleaf/master --no-commit --no-ff 2>/dev/null

# Restaurar archivos de configuración que no deben eliminarse
echo "Restaurando archivos de configuración..."
git checkout HEAD -- README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>/dev/null

# Restaurar carpeta PRUEBAS (proyecto Lean4, no viene de Overleaf)
git checkout HEAD -- PRUEBAS 2>/dev/null

# Completar el merge
if git diff --cached --quiet; then
    echo "No hay cambios nuevos desde Overleaf"
    git merge --abort 2>/dev/null
else
    git commit -m "Merge cambios desde Overleaf"
    echo ""
    echo "¡Sincronización completa!"
    echo "Cambios desde Overleaf aplicados correctamente"
fi
