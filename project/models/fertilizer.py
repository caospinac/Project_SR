from pony.orm import Required, Set

from .nutrient_set import NutrientSet


class Fertilizer(NutrientSet):
    name = Required(str, 40)
    presentation = Required(str, 20)
    
    recomendations = Set('Recomendation')
    fertilizer_prices = Set('FertilizerPrice')
