from pydantic import Schema, validator
from pydantic import BaseModel
from typing import List


class CreateUptade(BaseModel):
    id: str = Schema(None)
    status: str
    number: str
    client: str
    clientName: str
    modifiedUser: str
    typeTask: str = None
    ticketType: str
    currentUser: str
    priority: str
    category: str
    typeProblem: str
    modifiedWhen: str
    expectedResolutionDate: str = None
    parentId: str = None
    productCategory: List[str] = []
    city: str
    clientСategory: str = None
    segment: str = None
    commercialBrand: str = None
    clientBrand: str = None


class Notification(BaseModel):
    id: str
    user: str
