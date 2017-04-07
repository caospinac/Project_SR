if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *
from models.User import User


class Admin(User):
    """docstring for Lot"""
    pass
