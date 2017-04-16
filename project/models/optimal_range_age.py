from pony.orm import Required

from .nutrient_set import NutrientSet


class Optimal_range_age(NutrientSet):
    min = Required(float)
    max = Required(float)
    
    crop = Required('Crop')
