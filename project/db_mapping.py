from models.base import engine
from pony import orm


orm.sql_debug(True)

engine.bind("sqlite", "database.sqlite", create_db=True)
engine.generate_mapping(create_tables=True)
