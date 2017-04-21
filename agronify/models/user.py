from datetime import datetime

from pony.orm import (
    Optional, PrimaryKey, Required, Set
)

from .base import engine


class User(engine.Entity):
    _table_ = '_User'

    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    admin = Required(bool, default=False)
    firstname = Required(str, 40)
    lastname = Required(str, 40)
    email = Required(str, 64, unique=True)
    password = Required(str)
    phone = Optional(str, 15)

    lands = Set('Land', cascade_delete=True)
