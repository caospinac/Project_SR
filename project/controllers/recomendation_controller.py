from sanic.response import json
from .base_controller import BaseController


class RecomendationController(BaseController):
    def get(self, request):
        return json({'Recomendation': 'controller'})
