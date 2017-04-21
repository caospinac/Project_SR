from datetime import datetime
from uuid import uuid4

from sanic.response import json
from pony.orm import db_session, select

from .base_controller import BaseController
from models import Lab


class LabController(BaseController):
    async def post(self, request):
        req = request.form
        try:
            with db_session:
                if Lab.exists(email=req.get('email')):
                    return self.response_status(409)
                Lab(
                    **self.not_null_data(
                        id=uuid4().hex,
                        name=req.get('name'),
                        email=req.get('email'),
                        web=req.get('web'),
                        phone=req.get('phone'),
                        department=req.get('department'),
                        city=req.get('city'),
                        address=req.get('address'),
                        fertilizers=[],
                    )
                )
        except Exception as e:
            raise e
        return self.response_status(201)

    async def get(self, request, id):
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, select(
                        (x.id, x.name, x.email, x.web, x.phone,
                            x.department, x.city, x.address)
                        for x in Lab if x.active
                    )
                )
            if not Lab.exists(id=id):
                return self.response_status(404)
            return self.response_status(
                200, select(
                    (x.id, x.name, x.email, x.web, x.phone,
                        x.department, x.city, x.address)
                    for x in Lab if x.id == id and x.active
                )
            )

    async def patch(self, request, id):
        req = request.form
        with db_session:
            if not Lab.exists(id=id):
                return self.response_status(404)
            if req.get('email') and Lab.exists(email=req.get('email')):
                return self.response_status(409)
            try:
                Lab.get_for_update(id=id)
                changes = self.not_null_data(
                    name=req.get('name'),
                    email=req.get('email'),
                    web=req.get('web'),
                    phone=req.get('phone'),
                    department=req.get('department'),
                    city=req.get('city'),
                    address=req.get('address'),
                    active=req.get('active'),
                )
                Lab[id].set(**changes)
                return self.response_status(200, changes)
            except Exception as e:
                return self.response_status(202)

    async def delete(self, request, id):
        with db_session:
            if not Lab.exists(id=id):
                return self.response_status(404)
            try:
                Lab.get_for_update(id=id)
                Lab[id].set(
                    modified=datetime.now(),
                    active=False
                )
            except Exception as e:
                return self.response_status(500)
            else:
                return self.response_status(200, Lab[id].id)
