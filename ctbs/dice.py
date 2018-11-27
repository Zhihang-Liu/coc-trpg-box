import random


def dice(lv: int, rv: int) -> int:
    return random.randint(lv, rv)


def dice1d100() -> int:
    return dice(1, 100)


def dice1d6() -> int:
    return dice(1, 6)
