from pony.orm import Set, Optional, Required, PrimaryKey

from .base import engine


class Lab(engine.Entity):
    """docstring for Lot"""
    id_lab = PrimaryKey(int, auto=True)
    name = Required(str)
    phone = Optional(str, 10)
    prices_fertilizer = Set("PriceFertilizer")
