from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjunto:
    count = 0

    def __init__(self, nombre: str):
        self.elementos: list = []
        self.count += 1
        self.__id = self.count
        self.nombre: str = nombre

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        if elemento in self.elementos:
            return True
        else:
            return False

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, other):
        pass



if __name__ == "__main__":
    elemento_1: Elemento = Elemento("Hola")
    elemento_2: Elemento = Elemento("Adiós")
    elemento_3: Elemento = Elemento("Hola")
    print(elemento_1 == elemento_2)
    print(elemento_1 == elemento_3)
