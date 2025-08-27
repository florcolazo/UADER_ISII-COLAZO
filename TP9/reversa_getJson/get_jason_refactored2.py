"""Este módulo realiza la lectura de archivos JSON aplicando principios de ingeniería de software.""" #AGREGUE PARA SUBIR PUNTAJE 
import json
import sys
# A 
""" def cargar_datos():
    try:
        with open("sitedata.json", "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("No se encontró el archivo sitedata.json")
        sys.exit()
    except json.JSONDecodeError:
        print("El archivo sitedata.json no tiene formato JSON válido")
        sys.exit()

def obtener_clave():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "token1"

def main():
    datos = cargar_datos()
    clave = obtener_clave()

    if clave in datos:
        print(datos[clave])
    else:
        print("Clave no encontrada")

if __name__ == "__main__":
    main()
"""
#B

""" import json
import sys

class LectorJSON:
    def __init__(self, archivo="sitedata.json"):
        self.archivo = archivo
        self.datos = {}

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            print("No encontré el archivo.")
            sys.exit()
        except json.JSONDecodeError:
            print("Archivo JSON inválido.")
            sys.exit()

    def buscar(self, clave):
        if clave in self.datos:
            return self.datos[clave]
        else:
            return None

def obtener_clave():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "token1"

def main():
    lector = LectorJSON()
    lector.cargar()

    clave = obtener_clave()
    resultado = lector.buscar(clave)

    if resultado:
        print(resultado)
    else:
        print("Clave no encontrada.")

if __name__ == "__main__":
    main()
"""
# ======= Clase SingletonReader ========




""" class LectorJSON:
    def __init__(self, archivo="sitedata.json"):
        self.archivo = archivo
        self.datos = {}

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            print("No encontré el archivo.")
            sys.exit()
        except json.JSONDecodeError:
            print("Archivo JSON inválido.")
            sys.exit()

    def buscar(self, clave):
        if clave in self.datos:
            return self.datos[clave]
        else:
            return None

def obtener_clave():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "token1"

def main():
    lector = LectorJSON()
    lector.cargar()

    clave = obtener_clave()
    resultado = lector.buscar(clave)

    if resultado:
        print(resultado)
    else:
        print("Clave no encontrada.")

if __name__ == "__main__":
    main()
"""

#D
"""
import sys

# Interfaz común
class LectorBase:
    def cargar(self):
        raise NotImplementedError

    def buscar(self, clave):
        raise NotImplementedError


# Versión original adaptada a clase
class LectorOriginal(LectorBase):
    def __init__(self, archivo="sitedata.json"):
        self.archivo = archivo
        self.datos = {}

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                self.datos = json.load(f)
        except Exception as e:
            print(f"Error original: {e}")
            self.datos = None

    def buscar(self, clave):
        if self.datos is None:
            return None
        return self.datos.get(clave)


# Versión refactorizada con Singleton
class LectorSingleton(LectorBase):
    _instancia = None

    def __new__(cls, archivo="sitedata.json"):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.archivo = archivo
            cls._instancia.datos = {}
        return cls._instancia

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                self.datos = json.load(f)
        except Exception as e:
            print(f"Error singleton: {e}")
            self.datos = None

    def buscar(self, clave):
        if self.datos is None:
            return None
        return self.datos.get(clave)


def obtener_clave():
    if len(sys.argv) > 1 and sys.argv[1].strip():
        return sys.argv[1]
    return "token1"


def seleccionar_lector(modo="singleton"):
    if modo == "original":
        return LectorOriginal()
    else:
        return LectorSingleton()


def main():
    # Elegís qué versión usar: "original" o "singleton"
    lector = seleccionar_lector(modo="singleton")

    lector.cargar()
    if lector.datos is None:
        print("No se pudo cargar el archivo.")
        return

    clave = obtener_clave()
    resultado = lector.buscar(clave)

    if resultado is not None:
        print(resultado)
    else:
        print(f"Clave '{clave}' no encontrada.")


if __name__ == "__main__":
    main() """

#F Y G

"""
getJason.py
Programa para leer valores de un archivo JSON desde línea de comandos.

Propiedad de la compañía:
copyright UADERFCyT-IS2©2024 todos los derechos reservados

Este programa permite cargar datos desde un archivo JSON, buscar un valor por clave
y mostrarlo por pantalla. Implementa dos versiones del lector: la original y una
refactorizada con patrón Singleton, aplicando Branching by Abstraction para la migración.

El programa nunca termina con error de sistema, maneja errores controladamente.
"""

"""
getJason.py
Programa para leer valores de un archivo JSON desde línea de comandos.

Propiedad de la compañía:
copyright UADERFCyT-IS2©2024 todos los derechos reservados

Implementa dos versiones del lector JSON:
- OriginalReader (código original)
- SingletonReader (refactorizado con patrón Singleton)

Se elige la versión con un argumento, y el programa maneja errores controladamente.
"""

"""
get_jason_refactored.py
Programa para leer valores de un archivo JSON desde línea de comandos.

Propiedad de la compañía:
copyright UADERFCyT-IS2©2024 todos los derechos reservados

Implementa dos versiones del lector JSON:
- OriginalReader (código original)
- SingletonReader (refactorizado con patrón Singleton)

Se elige la versión con un argumento, y el programa maneja errores controladamente.
"""

"""
get_jason_refactored.py
Programa para leer datos JSON con patrón Singleton y original.

copyright UADERFCyT-IS2©2024 todos los derechos reservados
"""

"""
get_jason_refactored.py
Programa para leer datos JSON con patrón Singleton y original.

copyright UADERFCyT-IS2©2024 todos los derechos reservados
"""


"""
get_jason_refactored.py
Programa para leer datos JSON con patrón Singleton y original.

copyright UADERFCyT-IS2©2024 todos los derechos reservados
"""

"""
get_jason_refactored.py
Programa para leer datos desde un archivo JSON con dos versiones del lector:
- OriginalReader (implementación clásica)
- SingletonReader (refactorizada con patrón Singleton)

Se elige la versión a usar pasando la clave y el tipo como argumentos.
Si se invoca con -v, muestra la versión del programa.

copyright UADERFCyT-IS2©2024 todos los derechos reservados
"""

VERSION = "versión 1.1"

class BaseReader:
    """Interfaz base para lectores JSON."""
    def load(self):
        raise NotImplementedError

    def search(self, key):
        raise NotImplementedError


class OriginalReader(BaseReader):
    """Versión original del lector JSON."""

    def __init__(self, filename="sitedata.json"):
        self.filename = filename
        self.data = {}

    def load(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, IOError) as error:
            print(f"Error cargando archivo (original): {error}")
            self.data = None
        except json.JSONDecodeError:
            print("El archivo no contiene un JSON válido.")
            self.data = None

    def search(self, key):
        if self.data is None:
            return None
        return self.data.get(key)


class SingletonReader(BaseReader):
    """Versión refactorizada usando el patrón Singleton."""

    _instance = None

    def __new__(cls, filename="sitedata.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filename = filename
            cls._instance.data = {}
        return cls._instance

    def load(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, IOError) as error:
            print(f"Error cargando archivo (singleton): {error}")
            self.data = None
        except json.JSONDecodeError:
            print("El archivo no contiene un JSON válido.")
            self.data = None

    def search(self, key):
        if self.data is None:
            return None
        return self.data.get(key)


def get_args():
    """
    Procesa y valida argumentos de línea de comandos.
    Retorna una tupla: (clave, tipo_lector, mostrar_version)"""
    args = sys.argv[1:]

    if len(args) == 1 and args[0] == "-v":
        print(VERSION)
        return None, None, True

    if len(args) == 0:
        return "token1", "singleton", False

    if len(args) > 2:
        print("Error: Número de argumentos inválido.\n"
                "Uso: python get_jason_refactored.py [clave] [tipo]\n"
                "tipo puede ser 'original' o 'singleton'")
        return None, None, False

    key = args[0].strip()
    if not key:
        print("Error: la clave no puede estar vacía.")
        return None, None, False

    tipo = "singleton"
    if len(args) == 2:
        tipo = args[1].strip().lower()
        if tipo not in ("original", "singleton"):
            print("Error: tipo de lector inválido. Usar 'original' o 'singleton'.")
            return None, None, False

    return key, tipo, False


def select_reader(tipo="singleton"):
    """Devuelve el lector correspondiente al tipo solicitado."""
    if tipo == "original":
        return OriginalReader()
    return SingletonReader()


def main():
    """Función principal del programa."""
    key, tipo, show_version = get_args()

    if show_version or key is None or tipo is None:
        return

    reader = select_reader(tipo)
    reader.load()

    if reader.data is None:
        print("No se pudo cargar el archivo JSON.")
        return

    value = reader.search(key)
    if value is not None:
        print(value)
    else:
        print(f"Clave '{key}' no encontrada.")


if __name__ == "__main__":
    main()
