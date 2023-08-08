import numpy as np


# Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Vehiculo:
    def __init__(self, velocidad_maxima: float, kilometraje: float):
        self.velocidad_maxima: float = velocidad_maxima
        self.kilometraje: float = kilometraje


# Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:
    def __init__(self, coordenada_x: float, coordenada_y: float):
        self.coordenada_x: float = coordenada_x
        self.coordenada_y: float = coordenada_y

    # A la clase del punto anterior, defínale los siguientes métodos:
    # Un método mostrar que imprima por consola las coordenadas del punto
    def mostrar(self) -> None:
        print(f'({self.coordenada_x},{self.coordenada_y})')

    # Un método mover que cambie las coordenadas del punto
    def mover(self, mover_x: float, mover_y: float) -> None:
        self.coordenada_x = mover_x
        self.coordenada_y = mover_y

    # Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calcular_distancia(self, otro_x: float, otro_y: float) -> float:
        distancia = ((otro_x - self.coordenada_x) ** 2 + (otro_y - self.coordenada_y) ** 2) ** (1 / 2)
        return distancia


# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus
# esquinas.
class Rectangulo:
    def __init__(self, esquina_1: Punto, esquina_2: Punto):
        self.esquina_1: Punto = esquina_1
        self.esquina_2: Punto = esquina_2

    def lados(self) -> tuple:
        lado_1 = self.esquina_2.coordenada_x - self.esquina_1.coordenada_x
        if lado_1 < 0:
            lado_1 = lado_1 * -1
        lado_2 = self.esquina_2.coordenada_y - self.esquina_1.coordenada_y
        if lado_2 < 0:
            lado_2 = lado_2 * -1
        return lado_1, lado_2

    # Agregue métodos a la clase Rectángulo para calcular su perímetro
    def calcular_perimetro(self) -> float:
        lado_1, lado_2 = self.lados()
        perimetro = 2 * (lado_1 + lado_2)
        return perimetro

    # Calcular su área
    def calcular_area(self) -> float:
        lado_1, lado_2 = self.lados()
        area = lado_1 * lado_2
        return area

    # Indicar si el rectángulo es un cuadrado.
    def definir_cuadrado(self) -> None:
        lado_1, lado_2 = self.lados()
        if lado_1 == lado_2:
            print("Es cuadrado")
        else:
            print("No es cuadrado")


# Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el
# constructor.
class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro: Punto = centro
        self.radio: float = radio

    # Defina un método para calcular el área del círculo
    def calcular_area_circulo(self) -> float:
        area = np.pi * (self.radio ** 2)
        return area

    # El perímetro del círculo
    def calcular_perimetro_circulo(self) -> float:
        perimetro = 2 * np.pi * self.radio
        return perimetro

    # Indicar si un punto pertenece al círculo o no.
    def pertenece_al_circulo(self, punto: Punto) -> None:
        formula_pertenece = ((punto.coordenada_x - self.centro.coordenada_x) ** 2) + (
                (punto.coordenada_y - self.centro.coordenada_y) ** 2)
        if formula_pertenece == self.radio ** 2:
            print(f"El punto {(punto.coordenada_x, punto.coordenada_y)} pertenece a la circunferencia.")
        elif formula_pertenece < self.radio ** 2:
            print(f"El punto {(punto.coordenada_x, punto.coordenada_y)} es interior a la circunferencia.")
        else:
            print(f"El punto {(punto.coordenada_x, punto.coordenada_y)} es exterior a la circunferencia.")


# Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la
# construcción del objeto (se pasan como parámetros en el constructor).
class Carta:
    # Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
    PICAS = 1
    TREBOL = 2
    DIAMANTES = 3
    CORAZONES = 4

    def __init__(self, valor: int, pinta: int):
        self.valor: int = valor
        self.pinta: int = pinta


# Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los
# tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
class CuentaBancaria:
    def __init__(self, numero_cuenta: str, propietario: str):
        self.numero_cuenta: str = numero_cuenta
        self.propietario: str = propietario
        self.balance: float = 0

    # Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el
    # balance de la cuenta.
    def aplicar_cuota_manejo(self) -> None:
        self.balance *= 0.98

    # Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
    def depositar(self, deposito: float) -> None:
        self.balance = self.balance + deposito

    # Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
    def retirar(self, retiro: float) -> float:
        if retiro <= self.balance:
            self.balance -= retiro
            return retiro
        else:
            retiro = self.balance
            self.balance = 0
            return retiro

    # Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta
    # bancaria.
    def mostrar_detalles(self):
        print(f"El número de la cuenta es: {self.numero_cuenta}")
        print(f"El propietario de la cuenta es: {self.propietario}")
        print(f"El balance de la cuenta es: {self.balance}")
