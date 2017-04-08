from pony.orm import (
    Database, PrimaryKey, Required, Optional
)

from pony import orm


from datetime import datetime


engine = Database()
engine.bind(
    'sqlite', 'database.sqlite', create_db=True
)
orm.sql_debug(True)


class Auditable(object):
    """docstring for Auditable"""
    created = Required(
        datetime,
        default=datetime.utcnow
    )


class User(Auditable):
    """docstring for User"""
    id_user = PrimaryKey(int, auto=True)
    name = Required(str)
    lastname = Required(str)
    email = Required(str, 64, unique=True)
    phone = Optional(str)
    status = Required(bool)
    password = Required(str)
