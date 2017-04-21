from uuid import uuid4
from datetime import datetime

from pony.orm import db_session, select
from passlib.hash import pbkdf2_sha256

from config import SALT
from .base_controller import BaseController
from models import User


class UserController(BaseController):
    @staticmethod
    def crypt(value):
        return pbkdf2_sha256.hash(f'{value}{SALT}')

    async def post(self, request):
        req = request.form
        try:
            with db_session:
                if User.exists(email=req.get('email')):
                    return self.response_status(409)
                User(
                    **self.not_null_data(
                        id=uuid4().hex,
                        firstname=req.get('firstname'),
                        lastname=req.get('lastname'),
                        email=req.get('email'),
                        phone=req.get('phone'),
                        password=self.crypt(req.get('password')),
                        lands=[],
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
                        (u.id, u.firstname, u.lastname, u.email, u.phone)
                        for u in User if u.active
                    )
                )
            if not User.exists(id=id):
                return self.response_status(404)
            return self.response_status(
                200, select(
                    (u.firstname, u.lastname, u.email, u.phone)
                    for u in User if u.id == id and u.active
                )
            )

    async def patch(self, request, id):
        req = request.form
        with db_session:
            if not User.exists(id=id):
                return self.response_status(404)
            if req.get('email') and User.exists(email=req.get('email')):
                return self.response_status(409)
            try:
                User.get_for_update(id=id)
                changes = self.not_null_data(
                    modified=datetime.now(),
                    firstname=req.get('firstname'),
                    lastname=req.get('lastname'),
                    email=req.get('email'),
                    phone=req.get('phone'),
                )
                User[id].set(**changes)
                return self.response_status(200, changes)
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
                return self.response_status(200, User[id].id)
