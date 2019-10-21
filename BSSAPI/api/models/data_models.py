from pydantic import Schema, validator
from pydantic import BaseModel


class Notification(BaseModel):
    ClientName: str
    ClientAccount: str
    status: int
    ID: str = Schema(None, title='ID documentation',  min_length=3)
    Number: str
    ModifiedBy: int
    extendedMap: dict
