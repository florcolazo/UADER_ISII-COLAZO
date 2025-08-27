# Componente base
class Componente:
    def mostrar(self, nivel=0):
        raise NotImplementedError("Debe implementar el método mostrar().")


# Hoja (Leaf): representa una pieza individual
class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")


# Compuesto (Composite): puede contener otras piezas o subconjuntos
class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ SubConjunto: {self.nombre}")
        for c in self.componentes:
            c.mostrar(nivel + 1)


# Producto ensamblado principal
class ProductoPrincipal(SubConjunto):
    def __init__(self, nombre="Producto Principal"):
        super().__init__(nombre)


if __name__ == "__main__":
    # Crear producto principal
    producto = ProductoPrincipal()

    # Crear los 3 subconjuntos iniciales con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = SubConjunto(f"Subconjunto {i}")
        for j in range(1, 5):
            subconjunto.agregar(Pieza(f"Pieza {i}.{j}"))
        producto.agregar(subconjunto)

    # Mostrar configuración inicial
    print("Estructura inicial del producto:")
    producto.mostrar()

    # Agregar subconjunto opcional con 4 piezas
    subconjunto_opcional = SubConjunto("Subconjunto Opcional")
    for k in range(1, 5):
        subconjunto_opcional.agregar(Pieza(f"Pieza O.{k}"))
    producto.agregar(subconjunto_opcional)

    # Mostrar configuración final
    print("\nEstructura luego de agregar subconjunto opcional:")
    producto.mostrar()
