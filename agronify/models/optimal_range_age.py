from pony.orm import Required

from .nutrient_set import NutrientSet


class OptimalRangeAge(NutrientSet):
    min = Required(float)
    max = Required(float)

    crop = Required('Crop')
