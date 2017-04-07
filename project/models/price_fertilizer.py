from pony.orm import Required

from base import engine


class PriceFertilizer(engine.Entity):
    """docstring for Lot"""
    price = Required(float)
