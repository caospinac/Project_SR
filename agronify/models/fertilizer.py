from pony.orm import Required, Set

from .nutrient_set import NutrientSet


class Fertilizer(NutrientSet):
    _discriminator_ = '_Fertilizer'

    name = Required(str, 40)
    presentation = Required(str, 20)

    recomendations = Set('Recomendation')
    labs = Set('Lab')
