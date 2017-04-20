from sanic.response import json
from .base_controller import BaseController


class LabController(BaseController):
    async def get(self, request, arg):
        return json({'Lab': 'controller'})
