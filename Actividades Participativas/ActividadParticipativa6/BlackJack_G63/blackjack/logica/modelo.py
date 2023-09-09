class BlackJack:
    def __init__(self):
        self.jugador: Jugador = None
        self.casa: Casa = None
        self.baraja: Baraja = None


    def registrar_jugador(self, nombre):
        pass

    def iniciar_juego(self, apuesta):
        pass

    def hacer_jugada_jugador(self, tipo_jugada: bool) -> bool:
        pass

    def hacer_jugada_casa(self) -> bool:
        pass

    def finalizar_juego(self) -> bool:
        pass

    def comparar_manos(self, valor_mano_jugador: int, valor_mano_casa: int):
        pass


class Carta:
    def __init__(self, pinta: str, valor: str, tapada: bool):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = tapada


class Jugador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.fichas: int = 100


    def inicializar_mano(self, cartas):
        pass

    def valor_mano(self) -> int:
        pass

    def doblar_fichas(self):
        self.fichas *= 2

    def devolver_fichas(self, apuesta: int):
        self.fichas += apuesta

    def restar_fichas(self, apuesta: int):
        self.fichas -= apuesta


class Casa:
    def __init__(self):
        self.mano: Mano = None

    def inicializar_mano(self):
        pass

    def destapar_carta(self):
        pass

    def valor_mano(self) -> int:
        pass


class Baraja:
    def __init__(self, cartas: list[Carta]):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        pass




class Mano:
    def __init__(self, cartas: list[Carta]):
        self.cartas: list[Carta] = []


    def es_blackjack(self) -> bool:
        pass





