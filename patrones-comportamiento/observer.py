class Subject:
    def __init__(self):
        self._observers = []

    def notify(self, id_emitido):
        for observer in self._observers:
            observer.update(id_emitido)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class IDObserver:
    def __init__(self, id_propio):
        self.id_propio = id_propio

    def update(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"🟢 Coincidencia: el ID '{id_emitido}' fue reconocido por el observador {self.id_propio}")
        else:
            print(f"🔘 Observador {self.id_propio} no reacciona al ID '{id_emitido}'")


# MAIN

if __name__ == "__main__":
    emisor = Subject()

    # Crear observadores con sus IDs
    obs1 = IDObserver("A123")
    obs2 = IDObserver("B456")
    obs3 = IDObserver("C789")
    obs4 = IDObserver("D000")

    # Subscribirlos al emisor
    emisor.attach(obs1)
    emisor.attach(obs2)
    emisor.attach(obs3)
    emisor.attach(obs4)

    # Emitir 8 IDs (al menos 4 que coincidan)
    ids_a_emitir = ["X111", "B456", "Y222", "C789", "A123", "Z333", "D000", "AAAA"]

    for id_emitido in ids_a_emitir:
        print(f"\nEmitiendo ID: {id_emitido}")
        emisor.notify(id_emitido)
