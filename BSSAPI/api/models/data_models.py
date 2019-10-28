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
    ticketType: str = None
    currentUser: str = None
    priority: str = None
    category: str
    typeProblem: str
    modifiedWhen: str = None
    expectedResolutionDate: str = None
    parentId: str = None
    productCategory: List[str] = []
    city: str = None
    clientСategory: str = None
    segment: str = None
    commercialBrand: str = None
    marketingBrand: List[str] = []


class Notification(BaseModel):
    id: str
    user: str
