from pony.orm import PrimaryKey, Optional

from .base import engine


class Nutrient_set(engine.Entity):
    id = PrimaryKey(int, auto=True)
    potassium = Optional(float)
    phosphorus = Optional(float)
    nitrogen = Optional(float)
    organic_material = Optional(float)
    acidity = Optional(float)
    magnesium = Optional(float)
    nanganese = Optional(float)
    copper = Optional(float)
    sulfur = Optional(float)
    aluminum = Optional(float)
    iron = Optional(float)
    calcium = Optional(float)
