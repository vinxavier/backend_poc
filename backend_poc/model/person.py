
from backend_poc.model.base_model import BaseModel
from datetime import datetime
from sqlmodel import Column, DateTime, Field
from enum import Enum

class SystemRole(Enum):
    Admin = "Admin"
    User = "User"

class Person(BaseModel, table=True):
    cognito_id: str 
    first_name: str
    last_name: str 
    birthdate: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    email: str
    phone_number: str 
    system_role: SystemRole = Field(default=SystemRole.User)
    consents: str
    is_active: bool = Field(default=None)