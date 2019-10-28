from pydantic import Schema, validator
from pydantic import BaseModel
from typing import List


class Response(BaseModel):
    status: str
    success: bool = None
    message: str = ""
