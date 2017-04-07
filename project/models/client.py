from pony.orm import Set

from user import User


class Client(User):
    """docstring for User"""
    # id_cliente = PrimaryKey(int, auto=True)
    lands = Set("Land")
