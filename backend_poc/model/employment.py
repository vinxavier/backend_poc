from backend_poc.model.base_model import BaseModel
from sqlmodel import Field
from enum import Enum

class BusinessRole(Enum):
    CompanyAdmin = "CompanyAdmin"
    Member = "Member"
    Accountant = "Accountant"

class Employment(BaseModel, table=True):
    person_id: int = Field(foreign_key="person.id", primary_key=True, index=True, nullable=False)
    company_id: int = Field(foreign_key="company.id", primary_key=True, index=True, nullable=False)
    business_role: BusinessRole = Field(default=BusinessRole.Member, nullable=True)
    position: str