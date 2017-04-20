from pony.orm import Optional, Required

from .base import engine


class FertilizerPrice(engine.Entity):
    price = Optional(float)

    lab = Required('Lab')
    fertilizer = Required('Fertilizer')
