from pony.orm import PrimaryKey, Required
# Own

from base import engine


class Crop(engine.Entity):
    """docstring for Lot"""
    id_crop = PrimaryKey(int, auto=True)
    name = Required(str)
