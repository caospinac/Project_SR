from pony.orm import Set, PrimaryKey, Optional, Required

from base import engine


class Land(engine.Entity):
    """docstring for User"""
    # id_usuario = PrimaryKey(int, auto=True)
    id_land = PrimaryKey(int, auto=True)
    location = Optional(str)
    status = Required(bool)
    lots = Set("Lot")
    client = Required("Client")
