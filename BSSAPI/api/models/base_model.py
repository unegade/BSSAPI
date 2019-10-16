from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


class Model(BaseModel):
    def json(self):
        return jsonable_encoder(BaseModel.json(self))
