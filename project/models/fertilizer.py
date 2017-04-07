from pony.orm import Set
from models.Nutrients import Nutrients


class Fertilizer(Nutrients):
    """docstring for Lot"""
    recomendations = Set("Recomendation")
    prices_fertilizer = Set("PriceFertilizer")
