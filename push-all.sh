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

# Crear branch temporal desde master
git branch -D overleaf-sync 2>/dev/null
git checkout -b overleaf-sync master

# Eliminar archivos de configuración
git rm -f README.md .gitignore push-all.bat push-all.sh 2>/dev/null

# Eliminar archivos que no sean .tex ni .bib de "Notas para trabajar" y "RESUMEN DE REUNIONES"
echo "Filtrando archivos para Overleaf..."
find "Notas para trabajar" -type f ! -name "*.tex" ! -name "*.bib" -exec git rm -f {} \; 2>/dev/null
find "RESUMEN DE REUNIONES" -type f ! -name "*.tex" ! -name "*.bib" -exec git rm -f {} \; 2>/dev/null

# Commit los cambios
git commit -m "Remove config files and non-tex files for Overleaf sync" --no-verify 2>/dev/null

# Hacer push a Overleaf
echo "Subiendo a Overleaf..."
git push overleaf overleaf-sync:master

# Si falla, intentar con pull y merge
if [ $? -ne 0 ]; then
    echo "Sincronizando con Overleaf..."
    git pull overleaf master --no-edit --strategy-option theirs 2>/dev/null
    # Asegurarse de que los archivos sigan eliminados
    git rm -f README.md .gitignore push-all.bat push-all.sh 2>/dev/null
    find "Notas para trabajar" -type f ! -name "*.tex" ! -name "*.bib" -exec git rm -f {} \; 2>/dev/null
    find "RESUMEN DE REUNIONES" -type f ! -name "*.tex" ! -name "*.bib" -exec git rm -f {} \; 2>/dev/null
    git commit -m "Remove config files and non-tex files after merge" --no-verify 2>/dev/null
    git push overleaf overleaf-sync:master
fi

# Volver a master
git checkout master
git branch -D overleaf-sync

echo ""
echo "¡Sincronización completa!"
echo "- GitHub: con README, .gitignore y scripts"
echo "- Overleaf: solo carpetas de trabajo"
