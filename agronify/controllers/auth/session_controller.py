from passlib.hash import pbkdf2_sha256

from app import session_interface
from config import SALT
from controllers import BaseController
from models import User


class SessionController(BaseController):
    async def post(self, request):
        req = request.form
        email = requ.get('email')
        password = requ.get('password')
        try:
            us = User.select(lambda u: u.email == email).first()
            login = pbkdf2_sha256.verify(f"{password}{SALT}", us.password)
        except Exception as e:
            login = False
        if not login:
            return self.response_status(401)
        request['session']['us'] = us.id
        return self.response_status(200)
