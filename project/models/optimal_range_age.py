from pony.orm import PrimaryKey, Required

from .base import engine
from .nutrients import Nutrients


class OptimalRangeAge(Nutrients, engine.Entity):
    """docstring for Lot"""
    id_ora = PrimaryKey(int, auto=True)
    crop = Required("Crop")
    minimum = Required(float)
    maximum = Required(float)
