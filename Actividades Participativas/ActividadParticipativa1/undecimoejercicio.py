import random


def crear_lista_pares(cantidad: int):
    lista_pares = []
    while cantidad >= 1:
        numeros = random.randint(1, 100)
        if numeros%2 == 0:
            lista_pares.append(numeros)
            cantidad = cantidad-1

    return lista_pares

lista_pares = crear_lista_pares(100000)
print(lista_pares)

