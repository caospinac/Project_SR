if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.curdir)))

from models import Admin
from models import Card
from models import Client
from models import Crop
from models import Fertilizer
from models import Lab
from models import Land
from models import Lot
from models import Nutrients
from models import PriceFertilizer
from models import Recomendation
from models import User
from base import engine


engine.generate_mapping(create_tables=True)
