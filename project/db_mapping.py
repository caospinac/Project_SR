from models.base import db

db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)
