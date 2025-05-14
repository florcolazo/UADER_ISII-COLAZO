class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self._history = []  # pila de estados

    def save(self, writer):
        self._history.append(writer.save())

    def undo(self, writer):
        if self._history:
            writer.undo(self._history.pop())
        else:
            print("No hay más estados anteriores para deshacer.")


if __name__ == '__main__':
    import os
    os.system("clear")

    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n")

    print("se invoca al <undo>")
    caretaker.undo(writer)
    print(writer.content + "\n")

    print("se invoca al <undo>")
    caretaker.undo(writer)
    print(writer.content + "\n")

    print("se invoca al <undo> (no debería haber más estados)")
    caretaker.undo(writer)
    print(writer.content + "\n")

