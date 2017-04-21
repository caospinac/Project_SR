from datetime import datetime

from pony.orm import Optional, PrimaryKey, Required

from .base import engine


class Recomendation(engine.Entity):
    _table_ = '_Recomendation'

    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    score = Required(float, sql_default='NULL')

    card = Required('Card')
    fertilizer = Optional('Fertilizer')
