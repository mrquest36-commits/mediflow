from pydantic import BaseModel

from typing import Optional

from uuid import UUID

from datetime import datetime


class EncounterCreate(BaseModel):

    organization_id: UUID

    patient_id: UUID

    appointment_id: Optional[UUID] = None

    department_id: UUID

    recorded_by: UUID

    encounter_number: str

    encounter_type: str

    status: str = "open"

    description: Optional[str] = None


class EncounterResponse(BaseModel):

    id: UUID

    organization_id: UUID

    patient_id: UUID

    appointment_id: Optional[UUID]

    department_id: UUID

    recorded_by: UUID

    encounter_number: str

    encounter_type: str

    status: str

    description: Optional[str]

    started_at: datetime

    ended_at: Optional[datetime]

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True