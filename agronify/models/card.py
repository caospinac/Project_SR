from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Card(engine.Entity):
    id = PrimaryKey(str, 32)
    date = Required(datetime, sql_default='CURRENT_TIMESTAMP')

    nutrient_set = Required('NutrientSet')
    recomendations = Set('Recomendation')
    crop = Required('Crop')
