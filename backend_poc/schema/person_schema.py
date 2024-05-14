from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

from backend_poc.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from backend_poc.util.partial_model import partial_model


class BasePerson(BaseModel):
    cognito_id: str 
    first_name: str
    last_name: str 
    birthdate: datetime
    email: str
    phone_number: str 
    system_role: str
    consents: dict
    is_active: bool

    class Config:
        from_attributes = True



class BasePersonWithPassword(BasePerson):
    password: str

@partial_model
class Person(ModelBaseInfo, BasePerson):
    ...

@partial_model
class FindPerson(FindBase):
    ... 

@partial_model
class UpsertPerson(BasePerson):
    ...

class FindPersonResult(BaseModel):
    founds: Optional[List[Person]]
    search_options: Optional[SearchOptions]