from uuid import uuid4

from pony.orm import db_session
from sanic.response import json

from .base_controller import BaseController
from models import Land, User


class LandController(BaseController):
    async def post(self, request):
        req = request.form
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        try:
            with db_session:
                Land(
                    id=uuid4().hex,
                    state=req.get('state'),
                    city=req.get('city'),
                    address=req.get('address'),
                    user=User[user]
                )
        except Exception as e:
            raise e
        return self.response_status(201)

    async def get(self, request, arg):
        return json({'Land': 'controller'})
