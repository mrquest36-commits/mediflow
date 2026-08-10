from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class OrganizationBase(BaseModel):

    name: str
    code: str

    organization_type: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None



class OrganizationCreate(OrganizationBase):
    pass



class OrganizationResponse(OrganizationBase):

    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True