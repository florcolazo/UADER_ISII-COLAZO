# Implementación (Implementor)
class TrenLaminador:
    def producir(self, largo: float):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


# Implementaciones concretas (ConcreteImplementor)
class TrenLaminador5m(TrenLaminador):
    def producir(self, largo: float):
        if largo != 5:
            print("[Error] El tren de 5m solo produce láminas de 5 metros.")
        else:
            print("Produciendo lámina de acero de 0.5\" x 1.5m x 5m en el tren laminador de 5 metros.")


class TrenLaminador10m(TrenLaminador):
    def producir(self, largo: float):
        if largo != 10:
            print("[Error] El tren de 10m solo produce láminas de 10 metros.")
        else:
            print("Produciendo lámina de acero de 0.5\" x 1.5m x 10m en el tren laminador de 10 metros.")


# Abstracción (Abstraction)
class Lamina:
    def __init__(self, largo: float, tren: TrenLaminador):
        self.espesor = 0.5  # pulgadas
        self.ancho = 1.5    # metros
        self.largo = largo  # metros
        self.tren = tren    # referencia a la implementación

    def fabricar(self):
        print(f"[Lámina] Iniciando fabricación de lámina de {self.largo}m...")
        self.tren.producir(self.largo)

if __name__ == "__main__":
    tren5 = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    lamina1 = Lamina(5, tren5)
    lamina1.fabricar()  # Correcto

    lamina2 = Lamina(10, tren10)
    lamina2.fabricar()  # Correcto

    lamina3 = Lamina(5, tren10)
    lamina3.fabricar()  # Error lógico


