from datetime import datetime
from pony.orm import *


db = Database()


class Auditable(db.Entity):
    id = PrimaryKey(int, auto=True)
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    modified = Optional(datetime, sql_default='CURRENT_TIMESTAMP')
    active = Required(bool, default=True)


class Land(Auditable):
    location = Required(str)
    user = Required('User')


class User(Auditable):
    admin = Required(bool, default=True)
    firstname = Required(str, 40)
    lastname = Required(str, 40)
    email = Required(str, 64, unique=True)
    phone = Optional(str, 13)
    password = Required(str)
    lands = Set(Land, cascade_delete=True)


class Lot(Auditable):
    lot_name = Optional(str, 40)
    size = Required(float)
    crop = Required('Crop')
    cards = Set('Card')


class Nutrient_set(db.Entity):
    id = PrimaryKey(int, auto=True)
    potassium = Optional(float)
    phosphorus = Optional(float)
    nitrogen = Optional(float)
    organic_material = Optional(float)
    acidity = Optional(float)
    magnesium = Optional(float)
    nanganese = Optional(float)
    copper = Optional(float)
    sulfur = Optional(float)
    aluminum = Optional(float)
    iron = Optional(float)
    calcium = Optional(float)


class Card(Nutrient_set):
    crop_age = Required(float)
    date = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    lot = Required(Lot)
    recomendations = Set('Recomendation')


class Fertilizer(Nutrient_set):
    name = Required(str, 40)
    recomendations = Set('Recomendation')
    fertilizer_prices = Set('FertilizerPrice')


class Recomendation(Auditable):
    score = Required(float, sql_default='NULL')
    card = Required(Card)
    fertilizer = Optional(Fertilizer)


class Lab(Auditable):
    lab_name = Required(str, 40)
    lab_phone = Required(str, 13)
    fertilizer_prices = Set('FertilizerPrice')


class Crop(Auditable):
    crop_name = Required(str, 40)
    lots = Set(Lot)
    optimals_range_age = Set('Optimal_range_age')


class Optimal_range_age(Nutrient_set):
    min = Required(float)
    max = Required(float)
    crop = Required(Crop)


class FertilizerPrice(db.Entity):
    lab = Required(Lab)
    fertilizer = Required(Fertilizer)


db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)
