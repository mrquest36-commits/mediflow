from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Prescription(Base):

    __tablename__ = "prescriptions"

    encounter = relationship(
        "Encounter",
        back_populates="prescriptions"
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


    prescribed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    medication_name = Column(
        String(255),
        nullable=False
    )


    medication_code = Column(
        String(100),
        nullable=True
    )


    dosage = Column(
        String(100),
        nullable=True
    )


    frequency = Column(
        String(100),
        nullable=True
    )


    duration = Column(
        String(100),
        nullable=True
    )


    quantity = Column(
        Integer,
        nullable=True
    )


    instructions = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="active"
    )


    prescribed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
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