from sanic.response import json
from .base_controller import BaseController
from pony.orm import db_session, exists

from models import User


class UserController(BaseController):
    async def post(self, request):
        req = request.form
        print(request.form)
        with db_session:
            try:
                User(
                    firstname=req.get('firstname'),
                    lastname=req.get('lastname'),
                    email=req.get('email'),
                    phone=req.get('phone'),
                    password=req.get('password'),
                    lands=[],
                )
            except Exception as e:
                return self.response_status(409)
        return self.response_status(201)

    async def get(self, request, id):
        with db_session:
            if not exists(u for u in User if u.id == id):
                return self.response_status(404)
            return self.response_status(200, User[id])

    async def patch(self, request, id):
        req = request.form
        with db_session:
            if not exists(u for u in User if u.id == id):
                return self.response_status(404)
            try:
                User[id].set(
                    firstname=req.get('firstname'),
                    lastname=req.get('lastname'),
                    email=req.get('email'),
                    phone=req.get('phone'),
                    password=req.get('password'),
                    lands=[],
                )
            except Exception as e:
                pass
            else:
                return self.response_status(200, User[id])
        return self.response_status(204)

    async def delete(self, request, id):
        req = request.form
        with db_session:
            if not exists(u for u in User if u.id == id):
                return self.response_status(404)
            try:
                User[id].set(
                    active=False
                )
            except Exception as e:
                return self.response_status(500)
            else:
                return self.response_status(200, User[id])
