from pony.orm import Set, Required

from .nutrient_set import Nutrient_set


class Fertilizer(Nutrient_set):
    name = Required(str, 40)
    recomendations = Set('Recomendation')
    fertilizer_prices = Set('FertilizerPrice')
