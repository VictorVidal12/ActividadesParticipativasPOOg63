

def sumar_numeros_de_lista(lista: list):
    sumar_numeros = 0
    for j in range (len(lista)):
        sumar_numeros = lista[j] + sumar_numeros

    return sumar_numeros


print(sumar_numeros_de_lista([3,2,1,0,-3,2,5]))