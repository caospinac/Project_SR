from datetime import datetime
from pony.orm import PrimaryKey, Required, Database


engine = Database()


class Auditable(engine.Entity):
    id = PrimaryKey(str, 32)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)
