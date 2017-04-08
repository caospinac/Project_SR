from datetime import datetime
from pony.orm import *


db = Database()


class Auditable(db.Entity):
    id = PrimaryKey(int, auto=True)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Optional(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
