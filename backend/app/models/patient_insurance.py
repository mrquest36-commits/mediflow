from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class PatientInsurance(Base):

    __tablename__ = "patient_insurances"


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


    insurance_provider_id = Column(
        UUID(as_uuid=True),
        ForeignKey("insurance_providers.id"),
        nullable=False
    )


    membership_number = Column(
        String(255),
        nullable=False
    )


    policy_number = Column(
        String(255),
        nullable=True
    )


    is_primary = Column(
        Boolean,
        default=False
    )


    valid_from = Column(
        DateTime(timezone=True),
        nullable=True
    )


    valid_until = Column(
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