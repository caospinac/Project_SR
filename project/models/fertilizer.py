from pony.orm import Set, PrimaryKey, Required

from .base import engine
from .nutrients import Nutrients


class Fertilizer(Nutrients, engine.Entity):
    """docstring for Lot"""
    id_fertilizer = PrimaryKey(int, auto=True)
    name = Required(str)
    status = Required(bool, default=True)
    recomendations = Set("Recomendation")
    prices_fertilizer = Set("PriceFertilizer")
