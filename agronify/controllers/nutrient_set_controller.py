from sanic.response import json
from .base_controller import BaseController


class NutrientSetController(BaseController):
    async def get(self, request, arg):
        return json({'NutrientSet': 'controller'})
