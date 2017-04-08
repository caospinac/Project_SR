from models import Card
from models import Crop
from models import Fertilizer
from models import FertilizerPrice
from models import Lab
from models import Land
from models import Lot
from models import Nutrient_set
from models import Optimal_range_age
from models import Recomendation
from models import User
from models.base import db


db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)
