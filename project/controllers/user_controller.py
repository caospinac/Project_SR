from sanic.response import json
from .base_controller import BaseController
from pony.orm import db_session

from models import User


class UserController(BaseController):
    async def post(self, request):
        print(request.form)
        req = request.form
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
                print(e)
                return self.response_status(409)
            except Exception as e:
                print(e)
        return self.response_status(201)

    async def get(self, request, id):
        return json({'User': 'controller', 'request': str(request.args)})

    async def patch(self, request, id):
        return self.response_status(200)

    async def delete(self, request, id):
        if id:
            with db_session:
                try:
                    User[id].delete()
                except Exception as e:
                    print(e)
                    return self.response_status(404)
        return self.response_status(200)
