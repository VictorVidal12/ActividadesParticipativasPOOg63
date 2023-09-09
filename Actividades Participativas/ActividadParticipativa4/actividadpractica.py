
import numpy as np


def angulo_menor(horas: int, minutos: int) -> int:
    # Condición simple
    if horas*5 == minutos:
        return 0
    # Medimos los ángulos de dos formas diferentes
    # Éste mide el ángulo que se forma por la exterior de las manecillas
    angulo_1 = 360 - np.abs(horas*30 - minutos*6)
    # Éste mide el ángulo que se forma por la interior de las manecillas
    angulo_2 = np.abs(horas*30 - minutos*6)
    # Compara ambos ángulos para ver cuál es el menor y lo retorna
    if angulo_2 > angulo_1:
        return angulo_1
    else:
        return angulo_2


print(angulo_menor(12, 15))
