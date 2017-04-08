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
from models.base import engine


engine.generate_mapping(create_tables=True)
