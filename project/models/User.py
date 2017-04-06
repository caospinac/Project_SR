from server import *


class User(DB.Entity):
    """docstring for User"""
    id_usuario = PrimaryKey(int, auto=True)
    name = Required(str)
    lastname = Required(str)
    email = Required(str, 64, unique=True)
    phone = Optional(str)
    status = Required(bool)
    timestamp = Required(datetime)
    password = Required(str)
