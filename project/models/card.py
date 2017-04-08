from pony.orm import Required, Set, PrimaryKey
from .base import Auditable, engine

from .nutrients import Nutrients


class Card(Auditable, Nutrients, engine.Entity):
    """docstring for Lot"""
    id_card = PrimaryKey(int, auto=True)
    recomendations = Set("Recomendation")
    lot = Required("Lot")
