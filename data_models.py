from pydantic import BaseModel, Schema, validator

class Notification(BaseModel):
    ClientName: str
    ClientAccount: str
    status: int
    ID: str = Schema(None, title='ID documentation', max_length=300)
    Number: str
    ModifiedBy: int
    extendedMap: dict

    @validator('ClientName')
    def client_name_min_len(cls, v):
        if len(v) <= 3:
            raise ValueError('Length field ClientName is more three')
        return v