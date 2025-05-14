class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        if self.next_handler:
            self.next_handler.handle(number)
        else:
            print(f"Número {number} no consumido.")

class ParesHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"ParesHandler consumió el número: {number}")
        else:
            super().handle(number)

class PrimosHandler(Handler):
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"PrimosHandler consumió el número: {number}")
        else:
            super().handle(number)

# Crear la cadena: Primos -> Pares -> Ninguno
handler_chain = PrimosHandler(ParesHandler())

# Ejecutar para números del 1 al 100
for i in range(1, 101):
    handler_chain.handle(i)
