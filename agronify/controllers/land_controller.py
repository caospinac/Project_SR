from uuid import uuid4

from pony.orm import db_session, select
from sanic.response import json

from .base_controller import BaseController
from models import Land, User


class LandController(BaseController):
    async def post(self, request):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        req = request.form
        try:
            with db_session:
                Land(
                    id=uuid4().hex,
                    name=req.get('name'),
                    state=req.get('state'),
                    city=req.get('city'),
                    address=req.get('address'),
                    user=User[user],
                    lots=[]
                )
        except Exception as e:
            raise e
        return self.response_status(201)

    async def get(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, select(
                        l.id
                        for l in Land
                        if l.user == User[user] and l.active
                    )
                )
            if not Land.exists(id=id):
                return self.response_status(404)
            return self.response_status(200, Land[id])

    async def patch(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        req = request.form
        with db_session:
            if not Land.exists(id=id):
                return self.response_status(404)
            try:
                Land.get_for_update(id=id)
                Land[id].set(
                    **dict(
                        (k, v)
                        for k, v in dict(
                            modified=datetime.now(),
                            name=req.get('name'),
                            state=req.get('state'),
                            city=req.get('city'),
                            address=req.get('address'),
                        ).items()
                        if v
                    )
                )
                return self.response_status(200, Land[id])
            except Exception as e:
                return self.response_status(202)
