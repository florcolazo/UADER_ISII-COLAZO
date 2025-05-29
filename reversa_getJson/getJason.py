import json
import sys

with open("sitedata.json") as file:
    data = json.load(file)

# Usa el primer argumento o 'token1' como predeterminado
key = sys.argv[1] if len(sys.argv) > 1 else 'token1'

if key in data:
    print(data[key])
else:
    print("Clave no encontrada.")
