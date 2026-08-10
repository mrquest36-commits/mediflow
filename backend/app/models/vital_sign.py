from sqlalchemy import (
    Column,
    Numeric,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class VitalSign(Base):

    __tablename__ = "vital_signs"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    encounter = relationship(
        "Encounter",
        back_populates="vital_signs"
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

    recorded_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    temperature = Column(
        Numeric(5,2),
        nullable=True
    )


    pulse_rate = Column(
        Numeric(5,2),
        nullable=True
    )


    respiratory_rate = Column(
        Numeric(5,2),
        nullable=True
    )


    systolic_pressure = Column(
        Numeric(5,2),
        nullable=True
    )


    diastolic_pressure = Column(
        Numeric(5,2),
        nullable=True
    )


    oxygen_saturation = Column(
        Numeric(5,2),
        nullable=True
    )


    weight = Column(
        Numeric(6,2),
        nullable=True
    )


    height = Column(
        Numeric(6,2),
        nullable=True
    )


    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )