from datetime import datetime

from pony.orm import Optional, PrimaryKey, Required

from .base import engine


class Recomendation(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    score = Required(float, sql_default='NULL')
    
    card = Required('Card')
    fertilizer = Optional('Fertilizer')
