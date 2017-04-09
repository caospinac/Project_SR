from sanic.response import json
from .base_controller import BaseController


class FertilizerPriceController(BaseController):
    def get(self, request):
        return json({'FertilizerPrice': 'controller'})
