import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python getJason.py <sitedata> [clave]")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else 'token1'

    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        if jsonkey in obj:
            print(f"Valor para '{jsonkey}': {obj[jsonkey]}")
        else:
            print(f"Error: La clave '{jsonkey}' no existe en el archivo JSON.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{jsonfile}'.")
    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido.")

if __name__ == "__main__":
    main()
