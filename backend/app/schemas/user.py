from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):

    organization_id: UUID
    employee_id: str

    first_name: str
    last_name: str

    email: str
    password: str



class UserResponse(BaseModel):

    id: UUID

    organization_id: UUID
    employee_id: str

    first_name: str
    last_name: str

    email: str

    is_active: bool

    created_at: datetime


    class Config:
        from_attributes = True