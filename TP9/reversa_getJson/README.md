# getJason_REFACTORED.py

## Descripción

Este script es una versión refactorizada del programa original `getJason.pyc`, que pertenecía a un sistema legado sin código fuente accesible. El propósito principal es permitir la reutilización del programa para leer un archivo JSON (`sitedata.json`) y recuperar el valor asociado a una clave específica (por defecto, `token1`).

##  Requerimientos

- Python 3.6 o superior
- Archivo `sitedata.json` con contenido en formato clave-valor

## Estructura esperada del archivo `sitedata.json`

```json
{
  "token1": "C598-ECF9-F0F7-881A",
  "token2": "C598-ECF9-F0F7-881B"
}

