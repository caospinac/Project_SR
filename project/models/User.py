if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *


class User(DB.Entity):
    """docstring for User"""
    id_user = PrimaryKey(int, auto=True)
    name = Required(str)
    lastname = Required(str)
    email = Required(str, 64, unique=True)
    phone = Optional(str)
    status = Required(bool)
    timestamp = Required(datetime)
    password = Required(str)
