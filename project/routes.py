from controllers import (
    BaseController as Base,
    CardController as Card,
    CropController as Crop,
    FertilizerController as Fertilizer,
    FertilizerPriceController as FertilizerPrice,
    LabController as Lab,
    LandController as Land,
    LotController as Lot,
    NutrientSetController as NutrientSet,
    OptimalRangeAgeController as OptimalRangeAge,
    RecomendationController as Recomendation,
    UserController as User
)


view_route_list = [

    # Base routes
    (Base.as_view(), '/base'),

    # Base routes
    (Base.as_view(), '/base/<arg>'),

    # Card routes
    (Card.as_view(), '/card'),

    # Crop routes
    (Crop.as_view(), '/crop'),

    # Fertilizer routes
    (Fertilizer.as_view(), '/fertilizer'),

    # FertilizerPrice routes
    (FertilizerPrice.as_view(), '/fertilizer_price'),

    # Lab routes
    (Lab.as_view(), '/lab'),

    # Land routes
    (Land.as_view(), '/land'),
    (Land.as_view(), '/land/<id:\w{32}>'),
    (Land.as_view(), '/land/<id:all>'),

    # Lot routes
    (Lot.as_view(), '/lot'),
    (Lot.as_view(), '/lot/<id:\w{32}>'),
    (Lot.as_view(), '/lot/<id:all>'),

    # NutrientSet routes
    (NutrientSet.as_view(), '/nutrientset'),

    # OptimalRangeAge routes
    (OptimalRangeAge.as_view(), '/optimal_range_age'),

    # Recomendation routes
    (Recomendation.as_view(), '/recomendation'),

    # User routes
    (User.as_view(), '/user'),
    (User.as_view(), '/user/<id:\w{32}>'),
    (User.as_view(), '/user/<id:all>'),
]
