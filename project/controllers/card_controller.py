from sanic.response import json
from .base_controller import BaseController


class CardController(BaseController):
    def get(self, request):
        return json({'Card': 'controller'})
