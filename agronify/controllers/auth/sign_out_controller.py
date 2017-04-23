from passlib.hash import pbkdf2_sha256
from pony.orm import db_session

from config import SALT
from controllers import BaseController
from models import User


class SignOutController(BaseController):
    async def post(self, request):
        try:
            del request['session']['user']
            del request['session']['auth']
        except KeyError as e:
            pass
        return self.response_status(200, us)
