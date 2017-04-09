from pony.orm import Required

from .base import engine


class FertilizerPrice(engine.Entity):
    lab = Required('Lab')
    fertilizer = Required('Fertilizer')
