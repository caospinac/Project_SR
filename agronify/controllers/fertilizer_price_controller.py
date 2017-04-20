from sanic.response import json
from .base_controller import BaseController


class FertilizerPriceController(BaseController):
    async def get(self, request, arg):
        return json({'FertilizerPrice': 'controller'})
