if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *


class Crop():
    """docstring for Lot"""
    id_crop = PrimaryKey(int, auto=True)
    name = Required(str)
