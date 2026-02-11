#!/bin/bash

echo "Subiendo a GitHub..."
git push origin master
if [ $? -ne 0 ]; then
    echo "Error al subir a GitHub"
    exit 1
fi

echo ""
echo "Preparando push a Overleaf (solo carpetas de trabajo)..."

# Crear branch temporal para Overleaf
git branch -D overleaf-sync 2>/dev/null
git checkout -b overleaf-sync

# Eliminar README y .gitignore solo de este branch
git rm --cached README.md .gitignore push-all.bat 2>/dev/null
git commit -m "Remove config files for Overleaf sync" --no-verify

# Hacer push a Overleaf
echo "Subiendo a Overleaf..."
git push overleaf overleaf-sync:master --force

# Volver a master
git checkout master
git branch -D overleaf-sync

echo ""
echo "¡Sincronización completa!"
echo "- GitHub: con README, .gitignore y push-all.bat"
echo "- Overleaf: solo carpetas de trabajo"
