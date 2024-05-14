from backend_poc.model.base_model import BaseModel
from sqlmodel import Field


class Company(BaseModel, table=True):
    address: str
    name: str
    country: str 
    id_number: str
    vat_number: str
    industry: str
    detailed_activity: str
    company_site: str
    size: int
    bank_account_country: str
    is_active: bool = Field(default=False)