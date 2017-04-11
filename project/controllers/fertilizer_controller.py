from sanic.response import json
from .base_controller import BaseController


class FertilizerController(BaseController):
    async def get(self, request, arg):
        return json({'Fertilizer': 'controller'})
