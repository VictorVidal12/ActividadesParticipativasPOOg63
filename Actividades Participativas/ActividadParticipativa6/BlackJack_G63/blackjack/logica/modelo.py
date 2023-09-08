class BlackJack:
    def __init__(self):
        self.jugador: Jugador = None
        self.casa: Casa = None
        self.baraja: Baraja = None


    def registrar_jugador(self, nombre):
        pass

    def iniciar_juego(self, apuesta):
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


class Casa:
    def __init__(self):
        self.mano: Mano = None

    pass


class Baraja:
    def __init__(self, cartas: list[Carta]):
        self.cartas: list[Carta] = []

    pass


class Mano:
    def __init__(self, cartas: list[Carta]):
        self.cartas: list[Carta] = []


    def es_blackjack(self) -> bool:
        pass





