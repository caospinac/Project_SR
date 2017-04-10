from sanic.response import json
from .base_controller import BaseController
from pony.orm import db_session

from models import User


class UserController(BaseController):
    def get(self, request):
        return json({'User': 'controller', 'request': str(request.args)})

    def post(self, request):
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
                return super(UserController, self).post(request)
            else:
                return json({
                    'success': {
                        'code': 'TASK_SUCCESSFUL',
                        'message': 'That task was successful',
                    }
                }, status=201)
