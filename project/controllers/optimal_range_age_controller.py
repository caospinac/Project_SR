from sanic.response import json
from .base_controller import BaseController


class OptimalRangeAgeController(BaseController):
    def get(self, request):
        return json({'OptimalRangeAge': 'controller'})
