from sanic.response import json
from .base_controller import BaseController


class CropController(BaseController):
    def get(self, request):
        return json({'Crop': 'controller'})
