from datetime import datetime

from pony.orm import Required, Set

from .nutrient_set import NutrientSet


class Card(NutrientSet):
    crop_age = Required(float)
    date = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    lot = Required('Lot')
    recomendations = Set('Recomendation')
