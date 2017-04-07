if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *


class Land(DB.Entity):
    """docstring for User"""
    # id_usuario = PrimaryKey(int, auto=True)
    id_land = PrimaryKey(int, auto=True)
    location = Optional(str)
    status = Required(bool)
    lots = Set("Lot")
    client = Required("Client")
