from sanic.response import json
from .base_controller import BaseController


class CardController(BaseController):
    async def get(self, request, arg):
        return json({'Card': 'controller'})
