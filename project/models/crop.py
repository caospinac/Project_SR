from pony.orm import Required, Set

from .base import Auditable


class Crop(Auditable):
    crop_name = Required(str, 40)
    lots = Set('Lot')
    optimals_range_age = Set('Optimal_range_age')
