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


class InsuranceSettlement(Base):

    __tablename__ = "insurance_settlements"


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


    insurance_claim_id = Column(
        UUID(as_uuid=True),
        ForeignKey("insurance_claims.id"),
        nullable=False
    )


    received_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    settlement_amount = Column(
        Numeric(12, 2),
        nullable=False
    )


    payment_reference = Column(
        String(255),
        nullable=True
    )


    payment_method = Column(
        String(100),
        nullable=False
    )


    notes = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="received"
    )


    settled_at = Column(
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