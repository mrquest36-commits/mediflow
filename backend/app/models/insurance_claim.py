from sqlalchemy import (
    Column,
    String,
    Numeric,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class InsuranceClaim(Base):

    __tablename__ = "insurance_claims"


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


    patient_insurance_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patient_insurances.id"),
        nullable=False
    )


    invoice_id = Column(
        UUID(as_uuid=True),
        ForeignKey("invoices.id"),
        nullable=False
    )


    submitted_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    claim_number = Column(
        String(100),
        nullable=False,
        unique=True
    )


    claim_amount = Column(
        Numeric(12, 2),
        nullable=False
    )


    approved_amount = Column(
        Numeric(12, 2),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="submitted"
    )


    rejection_reason = Column(
        Text,
        nullable=True
    )


    submitted_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    processed_at = Column(
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