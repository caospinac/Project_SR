from http import HTTPStatus

from pony.orm.serialization import to_dict
from pony.orm.core import Query
from sanic.views import HTTPMethodView
from sanic.response import json


class BaseController(HTTPMethodView):

    @staticmethod
    def response_status(code, data=None):
        try:
            status = dict(vars(HTTPStatus))['_value2member_map_'][code]
            return json({
                'status': status.phrase,
                'description': status.description,
                'code': status.value,
                'data': to_dict(data) if type(data) == Query else data
            }, status=status.value)
        except KeyError as e:
            print(e)
            return json({})

    @staticmethod
    def not_null_data(**kw):
        return dict(
            (k, v)
            for k, v in kw.items()
            if v
        )

    async def post(self, request, arg=None):
        return self.response_status(501)

    async def get(self, request, arg=None):
        return self.response_status(501)

    async def put(self, request, arg=None):
        return self.response_status(501)

    async def patch(self, request, arg=None):
        return self.response_status(501)

    async def delete(self, request, arg=None):
        return self.response_status(501)
