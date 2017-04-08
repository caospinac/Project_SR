from pony.orm import PrimaryKey, Optional, Required

from .base import engine


class Nutrients(object):
    """docstring for User"""
    potassium = Optional(float)
    match = Optional(float)
    nitrogen = Optional(float)
    organic_material = Optional(float)
    acidity = Optional(float)
    magnesium = Optional(float)
    Manganese = Optional(float)
    copper = Optional(float)
    sulfur = Optional(float)
    aluminum = Optional(float)
    iron = Optional(float)
    calcium = Optional(float)
