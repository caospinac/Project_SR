from sanic.response import json
from .base_controller import BaseController


class LandController(BaseController):
    async def post(self, request):
        req = request.form
        try:
            with db_session:
                User(
                    id=uuid4().hex,
                    state=req.get('state'),
                    city=req.get('city'),
                    address=req.get('address'),
                    # user=
                )
        except Exception as e:
            return super().post(request, None)
        return self.response_status(201)

    async def get(self, request, arg):
        return json({'Land': 'controller'})
