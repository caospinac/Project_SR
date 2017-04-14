from controllers import (
    BaseController,
    CardController,
    CropController,
    FertilizerController,
    FertilizerPriceController,
    LabController,
    LandController,
    LotController,
    NutrientSetController,
    OptimalRangeAgeController,
    RecomendationController,
    UserController
)


view_route_list = [
    (BaseController.as_view(), '/base'),
    (BaseController.as_view(), '/base/<arg>'),
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
    (UserController.as_view(), '/user/<id:\w{32}>'),
]
