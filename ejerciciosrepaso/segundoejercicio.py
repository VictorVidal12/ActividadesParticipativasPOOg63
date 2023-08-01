# Llamamos la liberia numpy para tomar el valor de pi
import numpy as np

def calcular_area_circulo(r: float):
    area_circulo = np.pi*(r**2)
    return area_circulo

print(calcular_area_circulo(2))
