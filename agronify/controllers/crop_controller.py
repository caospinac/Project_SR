from sanic.response import json
from .base_controller import BaseController


class CropController(BaseController):
    async def get(self, request, arg):
        return json({'Crop': 'controller'})
