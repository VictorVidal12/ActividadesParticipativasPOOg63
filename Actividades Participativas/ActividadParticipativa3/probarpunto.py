from clases import Punto


if __name__ == "__main__":
    punto = Punto(4, 4)
    punto.mostrar()
    punto.mover(9, 9)
    punto.mostrar()
    print(punto.calcular_distancia(4, 4))
