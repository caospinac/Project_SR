from pony.orm import Required

from .base import db


class FertilizerPrice(db.Entity):
    lab = Required('Lab')
    fertilizer = Required('Fertilizer')
