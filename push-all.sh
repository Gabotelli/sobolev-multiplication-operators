#!/bin/bash

echo "Subiendo a GitHub..."
git push origin master
if [ $? -ne 0 ]; then
    echo "Error al subir a GitHub"
    exit 1
fi

echo ""
echo "Preparando push a Overleaf (solo carpetas de trabajo)..."

# Fetch desde Overleaf para tener el estado actualizado
git fetch overleaf

# Crear branch temporal basado en el estado actual de Overleaf
git branch -D overleaf-sync 2>/dev/null
git checkout -b overleaf-sync overleaf/master

# Eliminar archivos de configuración si existen
if [ -f "README.md" ]; then git rm README.md; fi
if [ -f ".gitignore" ]; then git rm .gitignore; fi
if [ -f "push-all.bat" ]; then git rm push-all.bat; fi
if [ -f "push-all.sh" ]; then git rm push-all.sh; fi

# Si hay cambios, hacer commit
if ! git diff --cached --quiet; then
    git commit -m "Remove config files for Overleaf sync" --no-verify
fi

# Merge con master (trae los cambios de las carpetas)
git merge master --no-edit -X theirs

# Hacer push a Overleaf
echo "Subiendo a Overleaf..."
git push overleaf overleaf-sync:master

# Volver a master
git checkout master
git branch -D overleaf-sync

echo ""
echo "¡Sincronización completa!"
echo "- GitHub: con README, .gitignore y scripts"
echo "- Overleaf: solo carpetas de trabajo"
