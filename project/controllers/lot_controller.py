from sanic.response import json
from .base_controller import BaseController


class LotController(BaseController):
    def get(self, request):
        return json({'Lot': 'controller'})
