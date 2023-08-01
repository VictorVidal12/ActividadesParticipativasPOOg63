

def encontrar_maximo_y_minimo(lista: list):

    # Ciclo para encontrar el máximo.
    maximo = 0
    minimo = 0
    for j in range(len(lista)):
        if lista[j]>maximo:
            maximo = lista[j]

    # Ciclo para encontrar el mínimo.
    for j in range(len(lista)):
        minimo = lista[j]
        if lista[j]<minimo:
            minimo = lista[j]

    print(f"El número más grande de la lista es {maximo} y el más pequeño es {minimo}")
    return

encontrar_maximo_y_minimo([3,1,4,2,0,-1])
