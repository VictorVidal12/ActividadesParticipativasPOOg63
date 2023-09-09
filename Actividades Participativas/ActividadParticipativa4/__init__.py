
import random as rd
import numpy as np


# Dado dos enteros que indican la hora y los minutos muestre el ángulo
# menor entre las dos manecillas de un reloj análogo.
def angulo_menor(horas: int, minutos: int) -> int:
    # Tener en cuenta que las horas*30 y los minutos*6 me dan los valores enteros en grados.
    print(f"Horas : {horas}, Minutos: {minutos}")
    # Condicional dado que las manecillas estén en la misma posición
    if horas*5 == minutos:
        return 0
    # Condicional para sacar los grados cuando la manecillas de horas está en la posición 0
    if horas == 0:
        # Toma el ángulo formado en el lado izquierdo
        if minutos > 30:
            return 360 - minutos*6
        # Toma el ángulo formado en el lado derecho
        else:
            return minutos*6
    # Condicional para sacar los grados cuando la manecilla de minutos está en la posición 0
    elif minutos == 0:
        # Toma el ángulo formado en el lado izquierdo
        if horas > 6:
            return 360 - horas*30
        # Toma el ángulo en el lado derecho
        else:
            return horas*30
    # Condicional para cuando alguna de las dos manecillas está en el lado derecho
    elif minutos > 30 or horas > 6:
        # Éstas dos variables guardan los grados de ambos casos para luego compararlos
        # Y ver cuál de los dos es menor.
        grados_1 = 360 - np.abs(minutos*6 - horas*30)
        grados_2 = np.abs(minutos*6 - horas*30)
        # Se comparan los grados calculados y se retorna el menor.
        if grados_1 > grados_2:
            return grados_2
        else:
            return grados_1
    # Si no entra por ninguno de los otros condicionales, las manecillas se encuentran en el lado derecho
    # y basta con calcular la diferencia entre éstas
    else:
        return np.abs(minutos*6 - horas*30)


print(angulo_menor(rd.randint(0, 12), rd.randint(0, 60)))
