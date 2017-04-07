from pony.orm import Set, PrimaryKey, Optional, Required

from base import engine


class Lot(engine.Entity):
    """docstring for Lot"""
    id_lot = PrimaryKey(int, auto=True)
    name = Required(str)
    size = Required(float)
    status = Required(bool)
    cards = Set("Card")
    land = Required("Land")
    card = Optional("Card")
