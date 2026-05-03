#!/bin/bash

echo "Subiendo a GitHub..."
git push origin master
if [ $? -ne 0 ]; then
    echo "Error al subir a GitHub"
    exit 1
fi

echo ""
echo "Preparando push a Overleaf (3 carpetas limpias)..."
git fetch overleaf

git branch -D overleaf-sync 2>/dev/null
git checkout -b overleaf-sync master

# Recuperar "Artículos Base" desde Overleaf ANTES del commit para que no se borre allí
git checkout overleaf/master -- "Artículos Base" 2>/dev/null

# Eliminar archivos de configuración de la raíz
git rm -f README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>/dev/null

# Eliminar carpetas que no deben ir a Overleaf
git rm -rf PRUEBAS 2>/dev/null
git rm -rf "TFG_GABRIEL" 2>/dev/null

# Eliminar archivos de compilación LaTeX de las 3 carpetas principales
echo "Eliminando archivos de compilación..."
for dir in "Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES"; do
    if [ -d "$dir" ]; then
        find "$dir" -type f \( \
            -name "*.aux" -o -name "*.log" -o -name "*.out" -o \
            -name "*.toc" -o -name "*.synctex.gz" -o -name "*.bbl" -o \
            -name "*.blg" -o -name "*.bcf" -o -name "*.run.xml" -o \
            -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.idx" -o \
            -name "*.ind" -o -name "*.ilg" -o -name "*.bak" -o -name "*.pdf" \
        \) -exec git rm -f {} \; 2>/dev/null
    fi
done

git commit -m "Sync to Overleaf: remove config files and compilation artifacts" --no-verify 2>/dev/null

echo "Subiendo a Overleaf..."
git push overleaf overleaf-sync:master

if [ $? -ne 0 ]; then
    echo "Sincronizando con Overleaf..."
    git pull overleaf master --no-edit --strategy-option theirs 2>/dev/null
    
    # Re-aplicar eliminaciones después del merge
    git rm -f README.md .gitignore push-all.bat push-all.sh pull-overleaf.bat pull-overleaf.sh 2>/dev/null
    git rm -rf PRUEBAS 2>/dev/null
    git rm -rf "TFG_GABRIEL" 2>/dev/null
    
    for dir in "Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES"; do
        if [ -d "$dir" ]; then
            find "$dir" -type f \( \
                -name "*.aux" -o -name "*.log" -o -name "*.out" -o \
                -name "*.toc" -o -name "*.synctex.gz" -o -name "*.bbl" -o \
                -name "*.blg" -o -name "*.bcf" -o -name "*.run.xml" -o \
                -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.idx" -o \
                -name "*.ind" -o -name "*.ilg" -o -name "*.bak" -o -name "*.pdf" \
            \) -exec git rm -f {} \; 2>/dev/null
        fi
    done
    
    # Restaurar archivos desde master si fueron eliminados
    git checkout master -- "Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES" 2>/dev/null
    
    # Volver a limpiar basura de compilación
    for dir in "Plantilla TFM" "Notas para trabajar" "RESUMEN DE REUNIONES"; do
        if [ -d "$dir" ]; then
            find "$dir" -type f \( \
                -name "*.aux" -o -name "*.log" -o -name "*.out" -o \
                -name "*.toc" -o -name "*.synctex.gz" -o -name "*.bbl" -o \
                -name "*.blg" -o -name "*.bcf" -o -name "*.run.xml" -o \
                -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.idx" -o \
                -name "*.ind" -o -name "*.ilg" -o -name "*.bak" -o -name "*.pdf" \
            \) -exec git rm -f {} \; 2>/dev/null
        fi
    done
    
    # Recuperar "Artículos Base" desde el servidor de Overleaf
    git checkout overleaf/master -- "Artículos Base" 2>/dev/null
    
    git commit -m "Remove config and build artifacts after merge" --no-verify 2>/dev/null
    git push overleaf overleaf-sync:master
fi

git checkout master
git branch -D overleaf-sync

echo ""
echo "¡Sincronización completa!"
echo "- GitHub: con README, .gitignore y scripts"
echo "- Overleaf: Plantilla TFM, Notas para trabajar, RESUMEN DE REUNIONES (sin basura de compilación)"
