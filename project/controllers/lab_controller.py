from sanic.response import json
from .base_controller import BaseController


class LabController(BaseController):
    def get(self, request):
        return json({'Lab': 'controller'})
