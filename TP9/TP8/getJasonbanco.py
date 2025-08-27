import json
import sys

# Fondos fijos simulados
fondos = {
    "BancoNacion": 20000,
    "BancoProvincia": 10000
}

monto = 15000

def main():
    if len(sys.argv) < 2:
        print("Uso: python getJasonbanco.py <tokens>")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, 'r') as f:
            data = json.load(f)

        # Seleccionar banco según fondos
        if fondos["BancoNacion"] >= monto:
            banco = "BancoNacion"
        elif fondos["BancoProvincia"] >= monto:
            banco = "BancoProvincia"
        else:
            print("No hay fondos suficientes.")
            return

        if banco in data:
            print(f"Pago liberado con {banco} usando token: {data[banco]}")
        else:
            print(f"No se encontró token para {banco}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'.")
    except json.JSONDecodeError:
        print("Error: El archivo no tiene formato JSON válido.")

if __name__ == "__main__":
    main()

# Versión 1.2
#------# Reingeniería: Se automatiza la elección de banco y se balancean pagos

import json

#------# Reingeniería: Singleton para obtener claves desde el JSON
class TokenManager:
    _instance = None

    def __new__(cls, archivo='sitedata.json'):
        if cls._instance is None:
            cls._instance = super(TokenManager, cls).__new__(cls)
            with open(archivo, 'r') as file:
                cls._instance.tokens = json.load(file)
        return cls._instance

    def get_clave(self, token):
        return self.tokens.get(token, "Clave no encontrada")

#------# Reingeniería: Clase Cuenta para manejar saldos
class Cuenta:
    def __init__(self, token, saldo_inicial):
        self.token = token
        self.saldo = saldo_inicial

    def puede_pagar(self, monto):
        return self.saldo >= monto

    def pagar(self, monto):
        if self.puede_pagar(monto):
            self.saldo -= monto
            return True
        return False

#------# Reingeniería: Chain of Responsibility para decidir qué cuenta paga
class ManejadorPagos:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.turno = 0  # Alterna entre cuentas
        self.pagos = []  # Lista para registrar pagos (para el Iterator)

    def realizar_pago(self, pedido_id, monto):
        intentos = 0
        while intentos < len(self.cuentas):
            cuenta = self.cuentas[self.turno]
            if cuenta.puede_pagar(monto):
                cuenta.pagar(monto)
                token = cuenta.token
                clave = TokenManager().get_clave(token)
                self.pagos.append((pedido_id, token, clave, monto))
                print(f"Pedido {pedido_id} pagado con {token} usando clave {clave} por ${monto}")
                self.turno = (self.turno + 1) % len(self.cuentas)
                return True
            else:
                self.turno = (self.turno + 1) % len(self.cuentas)
                intentos += 1
        print(f"Pedido {pedido_id} no pudo pagarse por falta de saldo.")
        return False

    #------# Reingeniería: Iterator para listar pagos
    def listar_pagos(self):
        print("\nListado de pagos realizados:")
        for pedido in self.pagos:
            print(f"Pedido {pedido[0]} - Token: {pedido[1]}, Clave: {pedido[2]}, Monto: ${pedido[3]}")

#------# Programa principal para prueba
def main():
    # Crear las cuentas
    cuenta1 = Cuenta("token1", 1000)
    cuenta2 = Cuenta("token2", 2000)

    manejador = ManejadorPagos([cuenta1, cuenta2])

    # Realizar pagos de $500, simula varios pedidos
    for i in range(1, 7):
        manejador.realizar_pago(i, 500)

    # Listado final de pagos
    manejador.listar_pagos()

if __name__ == "__main__":
    main()

