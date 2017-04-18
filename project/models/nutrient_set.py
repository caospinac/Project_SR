from pony.orm import Optional, PrimaryKey

from .base import engine


class NutrientSet(engine.Entity):
    id = PrimaryKey(str, 32)
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
