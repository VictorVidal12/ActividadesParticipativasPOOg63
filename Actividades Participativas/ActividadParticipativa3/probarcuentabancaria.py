from clases import CuentaBancaria

if __name__ == "__main__":
    cuenta_1 = CuentaBancaria("1025760171", "Victor Manuel Vidal Becerra")
    cuenta_1.depositar(10000)
    print(cuenta_1.balance)
    retirar = cuenta_1.retirar(2000)
    print(retirar)
    retirar_2 = cuenta_1.retirar(10000)
    print(retirar_2)
    cuenta_1.mostrar_detalles()
