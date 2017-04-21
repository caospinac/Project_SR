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
                        nitrogen=req.get('nitrogen'),
                        phosphorus=req.get('phosphorus'),
                        potassium=req.get('potassium'),
                        magnesium=req.get('magnesium'),
                        calcium=req.get('calcium'),
                        sulfur=req.get('sulfur'),
                        zinc=req.get('zinc'),
                        manganese=req.get('manganese'),
                        iron=req.get('iron'),
                        copper=req.get('copper'),
                        boron=req.get('boron'),
                        organic_material=req.get('organic_material'),
                        acidity=req.get('acidity'),
                        aluminum=req.get('aluminum'),
                    )
                )
        except Exception as e:
            raise e
        return self.response_status(201)
