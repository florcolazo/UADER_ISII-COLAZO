from collections.abc import Iterator, Iterable


class StringIterator(Iterator):
    def __init__(self, collection: str, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self):
        if self._reverse:
            if self._position < 0:
                raise StopIteration
            value = self._collection[self._position]
            self._position -= 1
        else:
            if self._position >= len(self._collection):
                raise StopIteration
            value = self._collection[self._position]
            self._position += 1
        return value


class StringIterable(Iterable):
    def __init__(self, cadena: str):
        self._cadena = cadena

    def __iter__(self) -> StringIterator:
        return StringIterator(self._cadena)

    def get_reverse_iterator(self) -> StringIterator:
        return StringIterator(self._cadena, reverse=True)


# Uso de ejemplo
if __name__ == "__main__":
    texto = StringIterable("Hola")

    print("Recorrido normal:")
    for char in texto:
        print(char, end=" ")

    print("\n\nRecorrido inverso:")
    for char in texto.get_reverse_iterator():
        print(char, end=" ")
