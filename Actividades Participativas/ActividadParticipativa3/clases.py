import numpy as np


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


# Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def calcular_area_circulo(self):
        area = np.pi * (self.radio ** 2)
        return area

    def calcular_perimetro_circulo(self):
        perimetro = 2 * np.pi * self.radio
        return perimetro

    def pertenece_al_circulo(self, punto: Punto):
        formula_pertenece = ((punto.coordenada_x - self.centro.coordenada_x) ** 2) + ((punto.coordenada_y - self.centro.coordenada_y) ** 2)
        if formula_pertenece == self.radio**2:
            print(f"El punto {punto} pertenece a la circunferencia.")
        elif formula_pertenece < self.radio**2:
            print(f"El punto {punto} es interior a la circunferencia.")
        else:
            print(f"El punto {punto} es exterior a la circunferencia.")
        return
