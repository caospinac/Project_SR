if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *
from models.User import User


class Client(User):
    """docstring for User"""
    # id_cliente = PrimaryKey(int, auto=True)
    lands = Set("Land")
