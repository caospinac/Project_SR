from pony.orm import PrimaryKey, Required, Set
# Own

from .base import engine


class Crop(engine.Entity):
    """docstring for Lot"""
    id_crop = PrimaryKey(int, auto=True)
    name = Required(str)
    lots = Set("Lot")
    optimals_range_age = Set("OptimalRangeAge")
