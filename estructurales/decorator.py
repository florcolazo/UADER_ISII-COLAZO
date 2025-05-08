# Componente base
class Numero:
    def imprimir(self):
        raise NotImplementedError("Debe implementar el método imprimir().")

# Clase concreta (componente base real)
class NumeroConcreto(Numero):
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        return self.valor

# Decorador base
class OperacionDecorator(Numero):
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        return self.numero.imprimir()
    
class SumarDos(OperacionDecorator):
    def imprimir(self):
        return self.numero.imprimir() + 2


class MultiplicarPorDos(OperacionDecorator):
    def imprimir(self):
        return self.numero.imprimir() * 2


class DividirPorTres(OperacionDecorator):
    def imprimir(self):
        return self.numero.imprimir() / 3
    
if __name__ == "__main__":
    # Número base
    numero = NumeroConcreto(9)
    print(f"Valor original: {numero.imprimir()}")  # 9

    # Decoración 1: Sumar 2
    suma = SumarDos(numero)
    print(f"Después de sumar 2: {suma.imprimir()}")  # 11

    # Decoración 2: Multiplicar por 2
    multiplicado = MultiplicarPorDos(suma)
    print(f"Después de multiplicar por 2: {multiplicado.imprimir()}")  # 22

    # Decoración 3: Dividir por 3
    dividido = DividirPorTres(multiplicado)
    print(f"Después de dividir por 3: {dividido.imprimir()}")  # 22 / 3 ≈ 7.33

    # Otra forma: encadenado directo
    decorado_final = DividirPorTres(MultiplicarPorDos(SumarDos(NumeroConcreto(9))))
    print(f"Encadenado en una línea: {decorado_final.imprimir():.2f}")  # ≈ 7.33


