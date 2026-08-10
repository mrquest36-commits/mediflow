from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Admission(Base):

    __tablename__ = "admissions"

    encounter = relationship(
        "Encounter",
        back_populates="admissions"
    )


    patient = relationship(
        "Patient",
        back_populates="admissions"
    )


    ward = relationship(
        "Ward",
        back_populates="admissions"
    )

    bed_assignments = relationship(
        "BedAssignment",
        back_populates="admission"
    )

    occupancy_history = relationship(
        "BedOccupancyHistory",
        back_populates="admission"
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


    encounter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("encounters.id"),
        nullable=False
    )


    patient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patients.id"),
        nullable=False
    )


    admitted_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    admission_type = Column(
        String(50),
        nullable=False
    )


    admission_reason = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="admitted"
    )


    admitted_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    ward_id = Column(
        UUID(as_uuid=True),
        ForeignKey("wards.id"),
        nullable=True
    )

    discharged_at = Column(
        DateTime(timezone=True),
        nullable=True
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