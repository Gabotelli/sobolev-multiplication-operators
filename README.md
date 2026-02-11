# TFM - Repositorio de Trabajo

Este repositorio contiene el trabajo de investigación organizado en tres carpetas principales:

- **Artículos Base/** - Documentos y artículos de referencia
- **Notas para trabajar/** - Notas y desarrollos del trabajo
- **RESUMEN DE REUNIONES/** - Resúmenes de reuniones y discusiones

## Configuración de Git

El repositorio está sincronizado con dos repositorios remotos:

- **GitHub**: https://github.com/Gabotelli/tfm.git (incluye README y .gitignore)
- **Overleaf**: https://git.overleaf.com/68e79d3d788acc72d9f9ff40 (solo carpetas de trabajo)

## Comandos Principales

### Push (subir cambios)

**Opción 1 - Push a ambos repositorios** (recomendado):

```bash
git add .
git commit -m "Descripción de los cambios"
.\push-all.bat
```

El script `push-all.bat` sincroniza automáticamente:
- A GitHub: todo el contenido (README, .gitignore y carpetas)
- A Overleaf: solo las 3 carpetas de trabajo

**Opción 2 - Push solo a GitHub**:

```bash
git push
```

**Opción 3 - Push manual a Overleaf** (solo carpetas):

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
