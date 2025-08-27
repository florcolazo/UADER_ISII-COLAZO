''' 
Módulo que gestiona pagos automáticos entre dos cuentas utilizando los patrones 
Singleton, Chain of Responsibility e Iterator. Versión 1.2
'''

import json

#------# Reingeniería: Singleton para obtener claves desde un archivo JSON
class TokenManager:
    '''Clase Singleton para manejar claves asociadas a tokens de bancos.'''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TokenManager, cls).__new__(cls)
            cls._instance._load_tokens()
        return cls._instance

    def _load_tokens(self):
        '''Carga los tokens desde el archivo sitedata.json.'''
        with open('sitedata.json', 'r', encoding='utf-8') as f:
            self.tokens = json.load(f)

    def get_key(self, token_name):
        '''Devuelve la clave del token solicitado.'''
        return self.tokens.get(token_name, 'Clave no encontrada')


#------# Reingeniería: Clase Cuenta con lógica de pagos y saldos
class Cuenta:
    '''Representa una cuenta bancaria con saldo.'''
    def __init__(self, token, saldo):
        self.token = token
        self.saldo = saldo

    def puede_pagar(self, monto):
        '''Verifica si hay saldo suficiente para el pago.'''
        return self.saldo >= monto

    def pagar(self, monto):
        '''Descuenta el monto del saldo.'''
        if self.puede_pagar(monto):
            self.saldo -= monto
            return True
        return False


#------# Reingeniería: Handler de pagos usando Chain of Responsibility
class GestorPagos:
    '''Gestiona los pagos alternando entre cuentas disponibles.'''
    def __init__(self):
        self.cuentas = [Cuenta("token1", 1000), Cuenta("token2", 2000)]
        self.turno = 0
        self.pagos = []

    def procesar_pago(self, pedido_id, monto):
        '''Procesa el pago seleccionando una cuenta con saldo suficiente.'''
        for i in range(len(self.cuentas)):
            cuenta = self.cuentas[(self.turno + i) % 2]
            if cuenta.puede_pagar(monto):
                cuenta.pagar(monto)
                token = cuenta.token
                clave = TokenManager().get_key(token)
                self.pagos.append((pedido_id, token, monto))
                print(f"Pedido {pedido_id}: Pago ${monto} con {token} (clave: {clave})")
                self.turno = (self.turno + 1) % 2
                return
        print(f"Pedido {pedido_id}: No se pudo realizar el pago. Fondos insuficientes.")

    def mostrar_pagos(self):
        '''Muestra todos los pagos realizados en orden cronológico.'''
        for pedido_id, token, monto in self.pagos:
            print(f"Pedido {pedido_id}: ${monto} con {token}")


#------# Simulación de ejecución
if __name__ == "__main__":
    gestor = GestorPagos()
    pedidos = [(1, 500), (2, 500), (3, 500), (4, 500), (5, 500)]
    for pedido_id, monto in pedidos:
        gestor.procesar_pago(pedido_id, monto)

    print("\nListado de pagos realizados:")
    gestor.mostrar_pagos()
