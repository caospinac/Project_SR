from pony.orm import Required, Set
from base import Auditable

from nutrients import Nutrients


class Card(Auditable, Nutrients):
    """docstring for Lot"""
    recomendations = Set("Recomendation")
    lot = Required("Lot")
