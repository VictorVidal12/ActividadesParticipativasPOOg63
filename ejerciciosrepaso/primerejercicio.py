""" En éste módulo crearé el primer ejercicio de los ejercicios de repaso para POO
"""

def imprimir_nombre_edad():
    """
    Éste método pide el nombre y la edad para después imprimirlos en la consola
    :return: Nothing
    """
    nombre = str(input("Ingresar nombre: "))
    edad = str(input("Ingresar edad: "))
    print(f"Su nombre es {nombre} y su edad es de {edad} años")
    return


imprimir_nombre_edad()
