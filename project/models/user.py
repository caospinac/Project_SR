from pony.orm import (
    Required, Optional, Set
)

from .base import Auditable


class User(Auditable):
    admin = Required(bool, default=True)
    firstname = Required(str, 40)
    lastname = Required(str, 40)
    email = Required(str, 64, unique=True)
    phone = Optional(str, 13)
    password = Required(str)
    lands = Set("Land", cascade_delete=True)
