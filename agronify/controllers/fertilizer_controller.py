from uuid import uuid4
from datetime import datetime

from pony.orm import db_session, select

from .base_controller import BaseController
from models import Fertilizer


class FertilizerController(BaseController):
    async def post(self, request):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
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

    async def get(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if id == 'all':
                return self.response_status(
                    200, select(
                        (x.id, x.name, x.presentation)
                        for x in Fertilizer
                    )[:10]
                )
            if not Fertilizer.exists(id=id):
                return self.response_status(404)
            return self.response_status(
                200, select(
                    (x.name, x.presentation)
                    for x in Fertilizer if x.id == id
                )
            )

    async def patch(self, request, id):
        user = request['session'].get('user')
        if not user:
            return self.response_status(401)
        with db_session:
            if not Fertilizer.exists(id=id):
                return self.response_status(404)
            req = request.form
            try:
                Fertilizer.get_for_update(id=id)
                changes = self.not_null_data(
                    **dict(
                        (k, v)
                        for k, v in dict(
                            modified=datetime.now(),
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
                        ).items()
                        if v
                    )
                )
                Fertilizer[id].set(**changes)
                return self.response_status(200, changes)
            except Exception as e:
                return self.response_status(202)
