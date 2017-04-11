from pony.orm import Required, Set

from .base import Auditable


class Land(Auditable):
    location = Required(str)
    user = Required('User')
    lots = Set('Lot')
