if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *


class Lot(DB.Entity):
    """docstring for Lot"""
    id_lot = PrimaryKey(int, auto=True)
    name = Required(str)
    size = Required(float)
    status = Required(bool)
    cards = Set("Card")
    land = Required("Land")
    card = Optional("Card")
