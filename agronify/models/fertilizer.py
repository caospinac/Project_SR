from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Fertilizer(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    name = Required(str, 40)
    presentation = Required(str, 20)
    nutrient_set = Required('NutrientSet')
    recomendations = Set('Recomendation')
    labs = Set('Lab')
