# Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


# Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    # A la clase del punto anterior, defínale los siguientes métodos:
    # Un método mostrar que imprima por consola las coordenadas del punto
    def mostrar(self):
        print(f'({self.coordenada_x},{self.coordenada_y})')
        return

    # Un método mover que cambie las coordenadas del punto
    def mover(self, mover_x, mover_y):
        self.coordenada_x = mover_x
        self.coordenada_y = mover_y
        return

    # Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calcular_distancia(self, otro_x, otro_y):
        distancia = (otro_y - self.coordenada_y) / (otro_x - self.coordenada_x)
        return distancia


# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
class Rectangulo:
    def __init__(self, esquina_1: Punto, esquina_2: Punto):
        self.esquina_1 = esquina_1
        self.esquina_2 = esquina_2

    def lados(self):
        lado_1 = self.esquina_2.coordenada_x - self.esquina_1.coordenada_x
        if lado_1 < 0:
            lado_1 = lado_1 * -1
        lado_2 = self.esquina_2.coordenada_y - self.esquina_1.coordenada_y
        if lado_2 < 0:
            lado_2 = lado_2 * -1
        return lado_1, lado_2

    def calcular_perimetro(self) -> float:
        lado_1, lado_2 = self.lados()
        perimetro = 2 * (lado_1 + lado_2)
        return perimetro

    def calcular_area(self) -> float:
        lado_1, lado_2 = self.lados()
        area = lado_1 * lado_2
        return area

    def definir_cuadrado(self):
        lado_1, lado_2 = self.lados()
        if lado_1 == lado_2:
            print("Es cuadrado")
        else:
            print("No es cuadrado")
        return

