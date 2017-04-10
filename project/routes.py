from controllers import BaseController
from controllers import CardController
from controllers import CropController
from controllers import FertilizerController
from controllers import FertilizerPriceController
from controllers import LabController
from controllers import LandController
from controllers import LotController
from controllers import NutrientSetController
from controllers import OptimalRangeAgeController
from controllers import RecomendationController
from controllers import UserController


view_route_list = [
    (BaseController.as_view(), '/base'),
    (CardController.as_view(), '/card'),
    (CropController.as_view(), '/crop'),
    (FertilizerController.as_view(), '/fertilizer'),
    (FertilizerPriceController.as_view(), '/fertilizer_price'),
    (LabController.as_view(), '/lab'),
    (LandController.as_view(), '/land'),
    (LotController.as_view(), '/lot'),
    (NutrientSetController.as_view(), '/nutrientset'),
    (OptimalRangeAgeController.as_view(), '/optimal_range_age'),
    (RecomendationController.as_view(), '/recomendation'),
    (UserController.as_view(), '/user'),
]
