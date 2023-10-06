from abc import abstractmethod, ABC


class Game:
    def __init__(self):
        pass

    def roll(self, pins: int):
        pass

    def score(self):
        pass


class Frame(ABC):
    @abstractmethod
    def add_roll(self, pins: int):
        pass

    def if_is_spare(self) -> bool:
        pass

    def if_is_strike(self) -> bool:
        pass

    @abstractmethod
    def score(self) -> int:
        pass


class TenthFrame(Frame):

    def add_roll(self, pins: int):
        return Roll(pins)

    def if_is_spare(self) -> bool:
        return super().if_is_spare()

    def if_is_strike(self) -> bool:
        return super().if_is_strike()

    def score(self) -> int:
        score = 0
        if self.if_is_spare():
            return score
        elif self.if_is_strike():
            return score
        else:
            return score


class NormalFrame(Frame):

    def add_roll(self, pins: int):
        return Roll(pins)

    def score(self) -> int:
        score = 0
        if self.if_is_spare():
            return score
        elif self.if_is_strike():
            return score
        else:
            return score

    def if_is_spare(self) -> bool:
        return super().if_is_spare()

    def if_is_strike(self) -> bool:
        return super().if_is_strike()


class Roll:
    def __init__(self, pins: int):
        self.pins: int = 10 - pins
