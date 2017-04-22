from datetime import datetime

from pony.orm import (
    Optional, PrimaryKey, Required, Set
)

from .base import engine


class Lab(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    name = Required(str, 40)
    email = Optional(str, 64, nullable=True)
    web = Optional(str, nullable=True)
    phone = Required(str)
    department = Required(str, 32)
    city = Required(str, 32)
    address = Required(str)

    fertilizers = Set('Fertilizer')
