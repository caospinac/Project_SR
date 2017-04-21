from datetime import datetime
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
                    **self.not_null_data(
                        id=uuid4().hex,
                        name=req.get('name'),
                        state=req.get('state'),
                        city=req.get('city'),
                        address=req.get('address'),
                        user=User[user],
                        lots=[]
                    )
                )
        except Exception as e:
            self.response_status(500)
        return self.response_status(201)

    async def get(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, select(
                        (l.id, l.name, l.state, l.city, l.address)
                        for l in Land
                        if l.user == User[user] and l.active
                    )
                )
            if not Land.exists(id=id):
                return self.response_status(404)
            return self.response_status(
                200, select(
                    (l.name, l.state, l.city, l.address)
                    for l in Land if l.id == id and l.active
                )
            )

    async def patch(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if not Land.exists(id=id):
                return self.response_status(404)
            if Land[id].user.id != user:
                return self.response_status(401)
            req = request.form
            try:
                Land.get_for_update(id=id)
                changes = self.not_null_data(
                    **dict(
                        (k, v)
                        for k, v in dict(
                            modified=datetime.now(),
                            name=req.get('name'),
                            state=req.get('state'),
                            city=req.get('city'),
                            address=req.get('address'),
                            active=req.get('active'),
                        ).items()
                        if v
                    )
                )
                Land[id].set(**changes)
                return self.response_status(200, changes)
            except Exception as e:
                return self.response_status(202)

    async def delete(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if not Land.exists(id=id):
                return self.response_status(404)
            if Land[id].user.id != user:
                return self.response_status(401)
            try:
                Land.get_for_update(id=id)
                Land[id].set(
                    modified=datetime.now(),
                    active=False
                )
            except Exception as e:
                raise e
            else:
                return self.response_status(200, Land[id].id)
