from pony.orm import Required

from .nutrient_set import Nutrient_set


class Optimal_range_age(Nutrient_set):
    min = Required(float)
    max = Required(float)
    crop = Required('Crop')
