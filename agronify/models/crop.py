from datetime import datetime

from pony.orm import Optional, PrimaryKey, Required, Set

from .base import engine


class Crop(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    name = Required(str, 40)
    lot_name = Required(str, 64, default='Unnamed')
    lot_size = Optional(float)

    land = Required('Land')
    cards = Set('Card')
