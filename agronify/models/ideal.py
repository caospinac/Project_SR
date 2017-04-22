from pony.orm import PrimaryKey, Required

from .base import engine


class Ideal(engine.Entity):
    id = PrimaryKey(str, 32)
    crop = Required(str, 32)
    nutrient = Required(str, 32)
    unit = Required(str, 8, default="%")
    min = Required(float)
    max = Required(float)
