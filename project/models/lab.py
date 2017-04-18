from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Lab(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    lab_name = Required(str, 40)
    lab_phone = Required(str, 13)

    fertilizer_prices = Set('FertilizerPrice')
