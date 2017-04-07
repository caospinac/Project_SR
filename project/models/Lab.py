if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *


class Lab(DB.Entity):
    """docstring for Lot"""
    id_lab = PrimaryKey(int, auto=True)
    name = Required(str)
    phone = Optional(str, 10)
    prices_fertilizer = Set("PriceFertilizer")
