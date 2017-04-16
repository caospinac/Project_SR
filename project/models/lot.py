from datetime import datetime

from pony.orm import  Optional, PrimaryKey, Required, Set

from .base import engine


class Lot(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    lot_name = Optional(str, 40)
    size = Required(float)
    
    crop = Required('Crop')
    land = Required('Land')
    cards = Set('Card')
