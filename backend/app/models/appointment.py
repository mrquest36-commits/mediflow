from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    Time,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Appointment(Base):

    __tablename__ = "appointments"

    encounters = relationship(
        "Encounter",
        back_populates="appointment"
    )
    
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


    patient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patients.id"),
        nullable=False
    )


    staff_profile_id = Column(
        UUID(as_uuid=True),
        ForeignKey("staff_profiles.id"),
        nullable=False
    )


    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )


    appointment_date = Column(
        Date,
        nullable=False
    )


    appointment_time = Column(
        Time,
        nullable=False
    )


    appointment_type = Column(
        String(100),
        nullable=False
    )


    reason = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="scheduled"
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