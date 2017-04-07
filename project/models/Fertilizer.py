if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *
from models.Nutrients import Nutrients


class Fertilizer(Nutrients):
    """docstring for Lot"""
    recomendations = Set("Recomendation")
    prices_fertilizer = Set("PriceFertilizer")
