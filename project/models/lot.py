from pony.orm import Set, Optional, Required

from .base import Auditable


class Lot(Auditable):
    lot_name = Optional(str, 40)
    size = Required(float)
    crop = Required('Crop')
    land = Required('Land')
    cards = Set('Card')
