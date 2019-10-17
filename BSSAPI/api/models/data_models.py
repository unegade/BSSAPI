from pydantic import Schema, validator
from BSSAPI.api.models.base_model import Model


class Notification(Model):
    ClientName: str
    ClientAccount: str
    status: int
    ID: str = Schema(None, title='ID documentation',  max_length=300,const=True)
    Number: str
    ModifiedBy: int
    extendedMap: dict

    @property
    def test(self):
        return len(self.ID)<2
    @validator('ClientName')
    def client_name_min_len(cls, v):
        if len(v) <= 3:
            raise ValueError('Length field ClientName is more three')
        return v