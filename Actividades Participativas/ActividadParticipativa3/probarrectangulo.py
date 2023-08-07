from clases import Punto, Rectangulo

if __name__ == "__main__":
    punto1 = Punto(3, 3)
    punto2 = Punto(8, 7)

    rectangulo = Rectangulo(punto1, punto2)
    print(rectangulo.lados())
    print(rectangulo.calcular_perimetro())
    print(rectangulo.calcular_area())
    rectangulo.definir_cuadrado()
