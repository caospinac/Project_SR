from sanic.response import json
from .base_controller import BaseController


class UserController(BaseController):
    def get(self, request):
        return json({'User': 'controller'})
