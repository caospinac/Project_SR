from sanic.response import json
from .base_controller import BaseController


class LandController(BaseController):
    async def get(self, request, arg):
        return json({'Land': 'controller'})
