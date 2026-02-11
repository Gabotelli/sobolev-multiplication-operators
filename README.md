# TFM - Repositorio de Trabajo

Este repositorio contiene el trabajo de investigación organizado en tres carpetas principales:

- **Artículos Base/** - Documentos y artículos de referencia
- **Notas para trabajar/** - Notas y desarrollos del trabajo
- **RESUMEN DE REUNIONES/** - Resúmenes de reuniones y discusiones

## Configuración de Git

El repositorio está configurado para sincronizarse automáticamente con:
- **GitHub**: https://github.com/Gabotelli/tfm.git
- **Overleaf**: https://git.overleaf.com/68e79d3d788acc72d9f9ff40

## Comandos Principales

### Push (subir cambios)
Cuando hagas un push, los cambios se sincronizarán automáticamente con **GitHub y Overleaf**:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
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
