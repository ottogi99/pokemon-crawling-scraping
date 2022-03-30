from enum import Enum


class PokeMonType(Enum):
    NORMAL = 0
    FLAME = 1
    WATER = 2
    GRASS = 3
    ELECTRIC = 4
    ICE = 5
    FIGHT = 6
    POISON = 7
    EARTH = 8
    FLIGHT = 9
    ESPER = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    OUCH = 15
    STEEL = 16
    FAIRY = 17


if __name__ == '__main__':
    print(PokeMonType.ELECTRIC.value)
