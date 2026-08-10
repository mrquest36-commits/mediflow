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


class TreatmentPlan(Base):

    __tablename__ = "treatment_plans"

    encounter = relationship(
        "Encounter",
        back_populates="treatment_plans"
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


    diagnosis_id = Column(
        UUID(as_uuid=True),
        ForeignKey("diagnoses.id"),
        nullable=True
    )


    prescribed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    treatment_type = Column(
        String(100),
        nullable=False
    )


    treatment_name = Column(
        String(255),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    start_date = Column(
        DateTime(timezone=True),
        nullable=True
    )


    end_date = Column(
        DateTime(timezone=True),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="active"
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