from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str


    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjunto:
    count: int = 0
    def __init__(self, nombre: str):
        self.elementos: list[Elemento] = []
        self.nombre: str = nombre
        self.count += 1
        self.__id: int = self.count

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def __add__(self, other):
        for elemento in other.elementos:
            if self.contiene(elemento):
                self.elementos.append(elemento)
        return self.elementos
    def agregar_elemento(self, elemento: Elemento) -> None:
        if self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        if isinstance(otro_conjunto, Conjunto):
            self.elementos + otro_conjunto

    @classmethod
    def intersectar(cls, conjunto_1, conjunto_2):
        conjunto_3: Conjunto = Conjunto("conjunto 3")
        for elemento in conjunto_1.elementos:
            for element in conjunto_2.elementos:
                if element == elemento:
                    conjunto_3.agregar_elemento(element)
        return conjunto_3

    def __str__(self) -> str:
        return f"Conjunto {self.nombre}: ({self.elementos}"



