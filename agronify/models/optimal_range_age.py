from pony.orm import Required

from .nutrient_set import NutrientSet


class OptimalRangeAge(NutrientSet):
    _discriminator_ = '_OptimalRangeAge'

    min = Required(float)
    max = Required(float)

    crop = Required('Crop')
