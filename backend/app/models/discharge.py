from sqlalchemy import (
    Column,
    Text,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Discharge(Base):

    __tablename__ = "discharges"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id"),
        nullable=False
    )


    admission_id = Column(
        UUID(as_uuid=True),
        ForeignKey("admissions.id"),
        nullable=False
    )


    patient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patients.id"),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="completed"
    )

    discharged_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    discharge_type = Column(
        String(100),
        nullable=False
    )


    final_diagnosis = Column(
        Text,
        nullable=True
    )


    hospital_course = Column(
        Text,
        nullable=True
    )


    discharge_condition = Column(
        String(100),
        nullable=False
    )


    instructions = Column(
        Text,
        nullable=True
    )


    follow_up_plan = Column(
        Text,
        nullable=True
    )


    discharged_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    disposition = Column(
        String(100),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )