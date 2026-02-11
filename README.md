# TFM - Repositorio de Trabajo

Este repositorio contiene el trabajo de investigación organizado en tres carpetas principales:

- **Artículos Base/** - Documentos y artículos de referencia
- **Notas para trabajar/** - Notas y desarrollos del trabajo
- **RESUMEN DE REUNIONES/** - Resúmenes de reuniones y discusiones

## Configuración de Git

El repositorio está sincronizado con dos repositorios remotos:

- **GitHub**: https://github.com/Gabotelli/tfm.git (todo el contenido)
- **Overleaf**: https://git.overleaf.com/68e79d3d788acc72d9f9ff40 (contenido filtrado)
  - Artículos Base: todos los archivos
  - Notas para trabajar: solo archivos .tex y .bib
  - RESUMEN DE REUNIONES: solo archivos .tex y .bib

## Comandos Principales

### Push (subir cambios)

**Opción 1 - Push a ambos repositorios** (recomendado):

En Windows (CMD):

```bash
git add .
git commit -m "Descripción de los cambios"
.\push-all.bat
```

En Git Bash / Linux / Mac:

```bash
git add .
git commit -m "Descripción de los cambios"
bash push-all.sh
```

Los scripts sincronizan automáticamente:

- A GitHub: todo el contenido (README, .gitignore, scripts y las 3 carpetas completas)
- A Overleaf: contenido filtrado
  - Artículos Base: todos los archivos
  - Notas para trabajar: solo archivos .tex y .bib
  - RESUMEN DE REUNIONES: solo archivos .tex y .bib

**Opción 2 - Push solo a GitHub**:

```bash
git push
```

**Opción 3 - Push manual a Overleaf**:

⚠️ **Nota**: Si haces push manual a Overleaf, también subirá README y .gitignore. Usa los scripts para mantener Overleaf solo con las carpetas de trabajo.

```bash
git push overleaf master
```

### Pull (traer cambios)

**Desde GitHub** (repositorio principal):

```bash
git pull
```

**Desde Overleaf** (si editaste directamente en Overleaf):

```bash
git pull overleaf master
```

## Estructura Protegida

El repositorio solo trackea archivos dentro de las tres carpetas principales. Cualquier archivo fuera de estas carpetas será ignorado automáticamente.
