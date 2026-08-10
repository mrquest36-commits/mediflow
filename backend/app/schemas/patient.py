from pydantic import BaseModel

from typing import Optional

from uuid import UUID

from datetime import datetime



class PatientCreate(BaseModel):

    organization_id: UUID

    patient_number: str

    first_name: str

    last_name: str

    date_of_birth: Optional[datetime] = None

    gender: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[str] = None

    address: Optional[str] = None



class PatientResponse(BaseModel):

    id: UUID

    organization_id: UUID

    patient_number: str

    first_name: str

    last_name: str

    date_of_birth: Optional[datetime]

    gender: Optional[str]

    phone: Optional[str]

    email: Optional[str]

    address: Optional[str]

    created_at: datetime


    class Config:

        from_attributes = True