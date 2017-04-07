if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

# Own
from database.base import *


class Nutrients(DB.Entity):
    """docstring for User"""
    id_nutrient = PrimaryKey(int, auto=True)
    potassium = Optional(float)
    match = Optional(float)
    nitrogen = Optional(float)
    organic_material = Optional(float)
    acidity = Optional(float)
    magnesium = Optional(float)
    Manganese = Optional(float)
    copper = Optional(float)
    sulfur = Optional(float)
    aluminum = Optional(float)
    iron = Optional(float)
    calcium = Optional(float)
