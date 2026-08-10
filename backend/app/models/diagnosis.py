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


class Diagnosis(Base):

    __tablename__ = "diagnoses"

    encounter = relationship(
        "Encounter",
        back_populates="diagnoses"
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


    recorded_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    diagnosis_code = Column(
        String(50),
        nullable=True
    )


    diagnosis_name = Column(
        String(255),
        nullable=False
    )


    diagnosis_type = Column(
        String(50),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    diagnosed_at = Column(
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