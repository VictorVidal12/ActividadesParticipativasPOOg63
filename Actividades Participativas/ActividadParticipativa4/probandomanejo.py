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
        nota_media = 0
        for j in self.estudiantes:
            nota_media += j.nota
        nota_media /= len(self.estudiantes)
        return nota_media


if __name__ == "__main__":
    estudiante1 = Estudiante('123', 'Victor', 2)
    estudiante2 = Estudiante('456', 'Vidal', 2)
    estudiante3 = Estudiante('789', 'Manuel', 3.1)
    estudiante4 = Estudiante('112', 'Becerra', 2)
    estudiante5 = Estudiante('134', 'Ismael', 1)
    curso11 = Curso()
    curso11.agregar_estudiante(estudiante1)
    curso11.agregar_estudiante(estudiante2)
    curso11.agregar_estudiante(estudiante3)
    curso11.agregar_estudiante(estudiante4)
    curso11.agregar_estudiante(estudiante5)
    print(curso11.nota_mediana())
    curso11.notas_a_cero()
    print(estudiante1.nota)
    print(estudiante2.nota)
    print(estudiante3.nota)
    print(estudiante4.nota)
    print(estudiante5.nota)
