import functools

from sanic.views import HTTPMethodView
from sanic.response import json
from http import HTTPStatus


class BaseController(HTTPMethodView):

    @staticmethod
    def response_status(code, message=None):
        try:
            status = dict(vars(HTTPStatus))['_value2member_map_'][code]
            return json({
                'status': status.phrase,
                'description': status.description,
                'code': status.value,
                'message': message
            }, status=status.value)
        except KeyError as e:
            print(e)
            return json({})

    async def post(self, request, arg):
        return self.__response_status(400)

    async def get(self, request, arg):
        return self.__response_status(404)

    async def put(self, request, arg):
        return self.__response_status(404)

    async def patch(self, request, arg):
        return self.__response_status(404)

    async def delete(self, request, arg):
        return self.response_status(404)
