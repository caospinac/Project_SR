from sanic.response import json
from .base_controller import BaseController


class LotController(BaseController):
    async def get(self, request, arg):
        return json({'Lot': 'controller'})
