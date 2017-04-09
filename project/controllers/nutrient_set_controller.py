from sanic.response import json
from .base_controller import BaseController


class NutrientSetController(BaseController):
    def get(self, request):
        return json({'NutrientSet': 'controller'})
