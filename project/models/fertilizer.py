from pony.orm import Set, Required

from .nutrient_set import NutrientSet


class Fertilizer(NutrientSet):
    name = Required(str, 40)
    recomendations = Set('Recomendation')
    fertilizer_prices = Set('FertilizerPrice')
    presentation = Required(str, 20)
