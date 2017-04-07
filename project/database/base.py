from pony.orm import Database, PrimaryKey, Required, Optional, Set
from pony import orm
from datetime import datetime


DB = Database()
DB.bind(
    'postgres',
    user='postgres', password='pgsql',
    host='localhost', database='fertilagro'
)

orm.sql_debug(True)
