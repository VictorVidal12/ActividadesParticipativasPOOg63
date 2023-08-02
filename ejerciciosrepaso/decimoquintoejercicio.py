

def determinar_palindromo(texto: str):
    # Creamos un texto auxiliar que contiene el mensaje original para después limpiarlo sin perderlo.
    textoAux = texto

    # Limpiamos la cadena de texto para que el palídromo no se vea influenciado por tildes, espacios o mayúsculas.
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")

    # Convertimos la cadena de texto en una lista con sus letras para mayor facilidad de manejo.
    lista_letras = list(texto)

    # Variables definidas para controlar el ciclo while.
    inicio = 0
    fin = len(lista_letras) - 1

    # Creamos un ciclo while válido mientras la primer letra del texto convertido en lista sea igual a la última.
    while lista_letras[inicio] == lista_letras[fin]:
        if inicio >= fin:
            print(f"La cadena de texto: '{textoAux}' es palíndroma.")
            return
        inicio = inicio + 1
        fin = fin - 1
    print(f"La cadena de texto: '{textoAux}' no es palíndroma.")
    return


determinar_palindromo("Dábale arroz a la zorra el abad")
determinar_palindromo("Allí ves Sevilla")
determinar_palindromo("A Mercedes ése de crema")
determinar_palindromo("Éste texto no es palíndromo")
determinar_palindromo("Dábale arro a la zorra el abad")