

def invertir_orden(lista: list):
    invertida = []
    for j in range(1, len(lista)+1):
        invertida.append(lista[-j])

    return invertida

print(invertir_orden([3,2,1]))