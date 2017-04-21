from datetime import datetime

from pony.orm import PrimaryKey, Required, Set

from .base import engine


class Crop(engine.Entity):
    _table_ = '_Crop'

    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
    name = Required(str, 40)

    lots = Set('Lot')
    optimals_range_age = Set('OptimalRangeAge')
