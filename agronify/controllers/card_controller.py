from uuid import uuid4
from datetime import datetime

from pony.orm import db_session, select

from .base_controller import BaseController
from models import Card, NutrientSet, Crop

class CardController(BaseController):
    async def post(self, request):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        req = request.form
        crop = request.args.get('crop')
        try:
            with db_session:
                ns = NutrientSet(
                    **self.not_null_data(
                        id=uuid4().hex,
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
                        al=req.get('al'),
                        organic_material=req.get('organic_material'),
                        acidity=req.get('acidity'),
                    )
                )
                Card(
                    **self.not_null_data(
                        id=uuid4().hex,
                        crop=Crop[crop],
                        nutrient_set=ns,
                    )
                )
        except Exception as e:
            raise e
        return self.response_status(201)

    async def get(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, Card.select()
                )
            if not Card.exists(id=id):
                return self.response_status(404)
            return self.response_status(
                200, Card.select(lambda x: x.id == id)
            )

    async def patch(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if not Card.exists(id=id):
                return self.response_status(404)
            req = request.form
            try:
                Card.get_for_update(id=id)
                ns_changes = self.not_null_data(
                    **dict(
                        modified=datetime.now(),
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
                        al=req.get('al'),
                        organic_material=req.get('organic_material'),
                        acidity=req.get('acidity'),
                    )
                )
                changes = self.not_null_data(
                    **dict(
                        id=uuid4().hex,
                        crop=Crop[crop],
                        nutrient_set=ns,
                    )
                )
                Card[id].set(**changes)
                Card[id].nutrient_set.set(**ns_changes)
                del ns_changes['modified']
                return self.response_status(200, dict(**changes, **ns_changes))
            except Exception as e:
                raise e
                return self.response_status(202)

    async def delete(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        req = request.form
        try:
            with db_session:
                Card.get_for_update(id=id)
                Card[id].delete()
        except Exception as e:
            raise e
        return self.response_status(200)
