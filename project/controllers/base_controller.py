from sanic.views import HTTPMethodView
from sanic.response import json


class BaseController(HTTPMethodView):       

    def get(self, request):
        return json({
            'error': {
                'code': 'TASK_NOT_FOUND',
                'message': 'That task was not found',
            }
        }, status=404)

    def post(self, request):
        return json({
            'error': {
                'code': 'TITLE_REQUIRED',
                'message': 'The title field is required',
            }
        }, status=400)

    def put(self, request):
        return json({
            'error': {
                'code': 'TASK_NOT_FOUND',
                'message': 'That task was not found',
            }
        }, status=404)

    def patch(self, request):
        return json({
            'error': {
                'code': 'TASK_NOT_FOUND',
                'message': 'That task was not found',
            }
        }, status=404)

    def delete(self, request):
        return json({
            'error': {
                'code': 'TASK_NOT_FOUND',
                'message': 'That task was not found',
            }
        }, status=404)
