

def media_aritmetica(lista: list):
    media = 0
    for j in range(len(lista)):
        media = media + lista[j]
    return media/len(lista)


print(media_aritmetica([3, 2, 1, 4, 10]))


