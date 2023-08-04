

def factorial(numero: int):
    factorial: int = 1
    while numero >= 1:
        factorial = factorial*(numero)
        numero = numero-1

    return factorial

print(factorial(10))