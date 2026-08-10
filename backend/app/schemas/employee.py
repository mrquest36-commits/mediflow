from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class EmployeeCreate(BaseModel):

    organization_id: UUID
    user_id: Optional[UUID] = None

    employee_number: str

    first_name: str
    last_name: str

    employee_type: str
    specialization: Optional[str] = None

    phone: Optional[str] = None
    email: Optional[str] = None


class EmployeeResponse(BaseModel):

    id: UUID

    organization_id: UUID
    user_id: Optional[UUID] = None

    employee_number: str

    first_name: str
    last_name: str

    employee_type: str
    specialization: Optional[str] = None

    phone: Optional[str] = None
    email: Optional[str] = None

    is_active: bool

    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True