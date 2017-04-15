from uuid import uuid4
from datetime import datetime

from .base_controller import BaseController
from pony.orm import db_session

from models import User


class UserController(BaseController):
    async def post(self, request):
        req = request.form
        print(request.form)
        try:
            with db_session:
                if User.exists(email=req.get('email')):
                    return self.response_status(409)
                User(
                    id=uuid4().hex,
                    firstname=req.get('firstname'),
                    lastname=req.get('lastname'),
                    email=req.get('email'),
                    phone=req.get('phone'),
                    password=req.get('password'),
                    lands=[],
                )
        except Exception as e:
            return super().post(request, None)
        return self.response_status(201)

    async def get(self, request, id):
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, User.select(lambda u: u.active)
                )
            if not User.exists(id=id):
                return self.response_status(404)
            return self.response_status(200, User[id])

    async def patch(self, request, id):
        req = request.form
        with db_session:
            if not User.exists(id=id):
                return self.response_status(404)
            if req.get('email') and User.exists(email=req.get('email')):
                return self.response_status(409)
            try:
                User.get_for_update(id=id)
                User[id].set(
                    **dict(
                        (k, v)
                        for k, v in dict(
                            modified=datetime.now(),
                            firstname=req.get('firstname'),
                            lastname=req.get('lastname'),
                            email=req.get('email'),
                            phone=req.get('phone'),
                            password=req.get('password'),
                        ).items()
                        if v
                    )
                )
                return self.response_status(200, User[id])
            except Exception as e:
                return self.response_status(202)

    async def delete(self, request, id):
        with db_session:
            if not User.exists(id=id):
                return self.response_status(404)
            try:
                User.get_for_update(id=id)
                User[id].set(
                    modified=datetime.now(),
                    active=False
                )
            except Exception as e:
                return self.response_status(500)
            else:
                return self.response_status(200, User[id])
