from datetime import datetime

from pony.orm import Required, PrimaryKey

from .base import engine


class NutrientSet(engine.Entity):
    _table_ = '_NutrientSet'

    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    nitrogen = Required(float, default=0)
    phosphorus = Required(float, default=0)
    potassium = Required(float, default=0)
    magnesium = Required(float, default=0)
    calcium = Required(float, default=0)
    sulfur = Required(float, default=0)
    zinc = Required(float, default=0)
    manganese = Required(float, default=0)
    iron = Required(float, default=0)
    copper = Required(float, default=0)
    boron = Required(float, default=0)
    organic_material = Required(float, default=0)
    acidity = Required(float, default=0)
    aluminum = Required(float, default=0)
