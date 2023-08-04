import random

def generar_matriz(filas: int, columnas: int):
    # Creamos una lista inicial vacía
    matriz = []
    for j in range(filas):
        # Agregamos listas para crear una matriz
        matriz.append([])
        for k in range(columnas):
            # Agregamos los números en la matriz
            matriz[j].append(random.randint(0, 9))
    return matriz

matriz = generar_matriz(5, 5)
print(matriz)

print(matriz[2][3])