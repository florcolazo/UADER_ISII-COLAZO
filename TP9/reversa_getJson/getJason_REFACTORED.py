# getJason_REFACTORED.py
# Autor: Florencia Colazo
# Fecha: 26-5-2025
# Descripción:
#   Este script realiza la lectura de un archivo JSON llamado 'sitedata.json'
#   y devuelve el valor correspondiente a una clave pasada como argumento por consola.
#   Si no se pasa ninguna clave, devuelve el valor asociado a 'token1'.

import json
import sys
import os

def cargar_datos_json(ruta_archivo):
    """Carga y devuelve los datos del archivo JSON especificado."""
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def obtener_valor(diccionario, clave):
    """Devuelve el valor asociado a la clave si existe, o un mensaje de error."""
    return diccionario.get(clave, f" Clave '{clave}' no encontrada en el archivo.")

def main():
    # Ruta al archivo JSON
    archivo_json = "sitedata.json"

    # Clave por defecto
    clave = sys.argv[1] if len(sys.argv) > 1 else "token1"

    try:
        datos = cargar_datos_json(archivo_json)
        resultado = obtener_valor(datos, clave)
        print(resultado)
    except Exception as error:
        print(f" Error: {error}")

if __name__ == "__main__":
    main()