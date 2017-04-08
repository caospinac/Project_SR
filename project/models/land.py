from pony.orm import Required

from .base import Auditable


class Land(Auditable):
    location = Required(str)
    user = Required('User')
