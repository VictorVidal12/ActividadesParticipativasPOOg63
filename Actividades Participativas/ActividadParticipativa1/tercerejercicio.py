import random


def crear_lista_aleatoria():
    cantidad_numeros = int(input("Ingrese la cantidad entera de números a imprimir en la lista: "))
    lista_aleatoria = []
    for j in range(cantidad_numeros):
        lista_aleatoria.append(random.randint(0, 10))
    return lista_aleatoria


print(crear_lista_aleatoria())
