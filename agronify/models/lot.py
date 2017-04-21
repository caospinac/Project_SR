from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Lot(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    name = Required(str, 40, nullable=True)
    size = Required(float)

    land = Required('Land')
    crop = Required('Crop')
    cards = Set('Card')
