from uuid import uuid4
from datetime import datetime

from pony.orm import db_session, select

from .base_controller import BaseController
from models import Fertilizer, Lab


class FertilizerController(BaseController):
    async def post(self, request):
        req = request.form
        try:
            with db_session:
                Fertilizer(
                    **self.not_null_data(
                        id=uuid4().hex,
                        name=req.get('name'),
                        presentation=req.get('presentation'),
                        n=req.get('n'),
                        p=req.get('p'),
                        k=req.get('k'),
                        mg=req.get('mg'),
                        ca=req.get('ca'),
                        s=req.get('s'),
                        zn=req.get('zn'),
                        mn=req.get('mn'),
                        fe=req.get('fe'),
                        cu=req.get('cu'),
                        b=req.get('b'),
                        organic_material=req.get('organic_material'),
                        acidity=req.get('acidity'),
                        aluminum=req.get('aluminum'),
                    )
                )
        except Exception as e:
            raise e
        return self.response_status(201)
