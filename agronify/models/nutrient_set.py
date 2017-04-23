from datetime import datetime

from pony.orm import Optional, PrimaryKey, Required

from .base import engine


class NutrientSet(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    n = Required(float, default=0)  # nitrogen
    p = Required(float, default=0)  # phosphorus
    k = Required(float, default=0)  # potassium
    mg = Required(float, default=0)  # magnesium
    ca = Required(float, default=0)  # calcium
    s = Required(float, default=0)  # sulfur
    zn = Required(float, default=0)  # zinc
    mn = Required(float, default=0)  # manganese
    fe = Required(float, default=0)  # iron
    cu = Required(float, default=0)  # copper
    b = Required(float, default=0)  # boron
    al = Required(float, default=0)  # aluminum
    organic_material = Required(float, default=0)
    acidity = Required(float, default=0)

    fertilizer = Optional('Fertilizer')
    card = Optional('Card')
