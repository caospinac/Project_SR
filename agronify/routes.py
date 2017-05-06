from controllers import (
    BaseController as Base,
    CardController as Card,
    CropController as Crop,
    FertilizerController as Fertilizer,
    LabController as Lab,
    LandController as Land,
    RecomendationController as Recomendation,
    UserController as User
)
from controllers.auth import (
    SignInController as SignIn,
    SignOutController as SignOut
)


api_routes = [

    # Base routes
    (Base.as_view(), '/api/base'),

    # Base routes
    (Base.as_view(), '/api/base/<arg>'),

    # Card routes
    (Card.as_view(), '/api/cards'),
    (Card.as_view(), '/api/cards/<id:\w{32}>'),
    (Card.as_view(), '/api/cards/<id:all>'),

    # Crop routes
    (Crop.as_view(), '/api/crops'),
    (Crop.as_view(), '/api/crops/<id:\w{32}>'),
    (Crop.as_view(), '/api/crops/<id:all>'),

    # Fertilizer routes
    (Fertilizer.as_view(), '/api/fertilizers'),
    (Fertilizer.as_view(), '/api/fertilizers/<id:\w{32}>'),
    (Fertilizer.as_view(), '/api/fertilizers/<id:all>'),

    # Lab routes
    (Lab.as_view(), '/api/labs'),
    (Lab.as_view(), '/api/labs/<id:\w{32}>'),
    (Lab.as_view(), '/api/labs/<id:all>'),

    # Land routes
    (Land.as_view(), '/api/lands'),
    (Land.as_view(), '/api/lands/<id:\w{32}>'),
    (Land.as_view(), '/api/lands/<id:all>'),

    # Recomendation routes
    (Recomendation.as_view(), '/api/recomendation'),

    # User routes
    (User.as_view(), '/api/users'),
    (User.as_view(), '/api/users/<id:\w{32}>'),
    (User.as_view(), '/api/users/<id:all>'),

    # SignIn routes
    (SignIn.as_view(), '/api/sign-in'),

    # SignOut routes
    (SignOut.as_view(), '/api/sign-out'),
]
