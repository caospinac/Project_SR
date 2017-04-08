from pony.orm import Required, Optional

from .base import Auditable


class Recomendation(Auditable):
    score = Required(float, sql_default='NULL')
    card = Required('Card')
    fertilizer = Optional('Fertilizer')
