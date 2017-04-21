from datetime import datetime

from pony.orm import  Optional, PrimaryKey, Required, Set

from .base import engine


class Lot(engine.Entity):
    _table_ = '_Lot'

    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    name = Optional(str, 40)
    size = Required(float)

    land = Required('Land')
    crop = Required('Crop')
    cards = Set('Card')
