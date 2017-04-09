from sanic.response import json
from .base_controller import BaseController


class FertilizerController(BaseController):
    def get(self, request):
        return json({'Fertilizer': 'controller'})
