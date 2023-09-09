class Estudiante:
    def __init__(self, id: str, nombre: str, nota: float):
        self.id: str = id
        self.nombre: str = nombre
        self.nota: float = nota


class Curso:
    def __init__(self):
        self.estudiantes: list = []

    def agregar_estudiante(self, estudiante: Estudiante) -> None:
        self.estudiantes.append(estudiante)

    def notas_a_cero(self) -> None:
        for j in self.estudiantes:
            if j.nota <= 3:
                j.nota = 0
            else:
                break

    def nota_mediana(self) -> float:
        for j in range(len(self.estudiantes)):
            for k in range(len(self.estudiantes)-1-j):
                if self.estudiantes[k].nota > self.estudiantes[k + 1].nota:
                    tupla = (self.estudiantes[k + 1].nota, self.estudiantes[k].nota)
                    self.estudiantes[k].nota, self.estudiantes[k + 1].nota = tupla
        if len(self.estudiantes) % 2 == 0:
            nota_1 = self.estudiantes[len(self.estudiantes)//2].nota
            nota_2 = self.estudiantes[(len(self.estudiantes)//2) - 1].nota
            mediana = (nota_1 + nota_2)/2
            return mediana
        else:
            return self.estudiantes[len(self.estudiantes)//2].nota


if __name__ == "__main__":
    estudiante1 = Estudiante('123', 'Victor', 5)
    estudiante2 = Estudiante('456', 'Vidal', 4)
    estudiante3 = Estudiante('789', 'Manuel', 3.4)
    estudiante4 = Estudiante('112', 'Becerra', 3.4)
    estudiante5 = Estudiante('134', 'Ismael', 2)
    estudiante6 = Estudiante('135', 'Ismaelo', 1)
    curso11 = Curso()
    curso11.agregar_estudiante(estudiante1)
    curso11.agregar_estudiante(estudiante2)
    curso11.agregar_estudiante(estudiante3)
    curso11.agregar_estudiante(estudiante4)
    curso11.agregar_estudiante(estudiante5)
    curso11.agregar_estudiante(estudiante6)
    print(curso11.nota_mediana())
