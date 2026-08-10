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


class Encounter(Base):

    __tablename__ = "encounters"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    patient = relationship(
        "Patient",
        back_populates="encounters"
    )

    admissions = relationship(
        "Admission",
        back_populates="encounter"
    )

    appointment = relationship(
        "Appointment",
        back_populates="encounters"
    )


    department = relationship(
        "Department",
        back_populates="encounters"
    )


    recorded_user = relationship(
        "User",
        back_populates="encounters"
    )


    vital_signs = relationship(
        "VitalSign",
        back_populates="encounter"
    )


    clinical_notes = relationship(
        "ClinicalNote",
        back_populates="encounter"
    )


    diagnoses = relationship(
        "Diagnosis",
        back_populates="encounter"
    )


    prescriptions = relationship(
        "Prescription",
        back_populates="encounter"
    )


    laboratory_orders = relationship(
        "LaboratoryOrder",
        back_populates="encounter"
    )


    imaging_orders = relationship(
        "ImagingOrder",
        back_populates="encounter"
    )


    treatment_plans = relationship(
        "TreatmentPlan",
        back_populates="encounter"
    )


    procedures = relationship(
        "Procedure",
        back_populates="encounter"
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

    appointment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
        nullable=True
    )


    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )

    recorded_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    encounter_number = Column(
        String(50),
        nullable=False,
        unique=True
    )


    encounter_type = Column(
        String(50),
        nullable=False
    )


    status = Column(
        String(50),
        nullable=False,
        default="open"
    )


    description = Column(
        Text,
        nullable=True
    )


    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    ended_at = Column(
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