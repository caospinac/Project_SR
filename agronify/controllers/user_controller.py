from uuid import uuid4
from datetime import datetime

from config import SALT
from .base_controller import BaseController
from pony.orm import db_session, select
from passlib.hash import pbkdf2_sha256

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
                    id=uuid4().hex,
                    firstname=req.get('firstname'),
                    lastname=req.get('lastname'),
                    email=req.get('email'),
                    phone=req.get('phone'),
                    password=self.crypt(req.get('password')),
                    lands=[],
                )
        except Exception as e:
            raise e
        return self.response_status(201)

    async def get(self, request, id):
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, select(u.id for u in User if u.active)
                )
            if not User.exists(id=id):
                return self.response_status(404)
            return self.response_status(
                200, User.select_by_sql('SELECT * FROM "_User" WHERE id = $id')
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
                User[id].set(
                    **dict(
                        (k, v)
                        for k, v in dict(
                            modified=datetime.now(),
                            firstname=req.get('firstname'),
                            lastname=req.get('lastname'),
                            email=req.get('email'),
                            phone=req.get('phone'),
                            password=self.crypt(req.get('password')),
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
