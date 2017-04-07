from pony.orm import (
    PrimaryKey, Required, Optional
)

# Own
from base import engine, Auditable


class User(Auditable, engine.Entity):
    """docstring for User"""
    id_user = PrimaryKey(int, auto=True)
    name = Required(str)
    lastname = Required(str)
    email = Required(str, 64, unique=True)
    phone = Optional(str)
    status = Required(bool)
    password = Required(str)
