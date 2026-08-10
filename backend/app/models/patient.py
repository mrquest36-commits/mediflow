from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base




class Patient(Base):

    __tablename__ = "patients"


    organization = relationship(
        "Organization",
        back_populates="patients"
    )

    admissions = relationship(
        "Admission",
        back_populates="patient"
    )

    encounters = relationship(
        "Encounter",
        back_populates="patient"
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


    patient_number = Column(
        String(50),
        nullable=False,
        unique=True
    )


    first_name = Column(
        String(100),
        nullable=False
    )


    last_name = Column(
        String(100),
        nullable=False
    )


    date_of_birth = Column(
        DateTime(timezone=True),
        nullable=True
    )


    gender = Column(
        String(20),
        nullable=True
    )


    phone = Column(
        String(30),
        nullable=True
    )


    email = Column(
        String(255),
        nullable=True
    )


    address = Column(
        Text,
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