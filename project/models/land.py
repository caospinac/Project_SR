from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Land(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    location = Required(str)

    user = Required('User')
    lots = Set('Lot')
