from pony.orm import Set, Required

from .base import Auditable


class Lab(Auditable):
    lab_name = Required(str, 40)
    lab_phone = Required(str, 13)
    fertilizer_prices = Set('FertilizerPrice')
