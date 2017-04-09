from sanic.response import json
from .base_controller import BaseController


class LandController(BaseController):
    def get(self, request):
        return json({'Land': 'controller'})
