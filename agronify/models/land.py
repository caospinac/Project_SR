from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Land(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    name = Required(str, 40)
    state = Required(str, 40)
    city = Required(str, 40)
    address = Required(str)

    user = Required('User')
    crops = Set('Crop')
