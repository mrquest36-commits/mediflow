from sqlalchemy import (
    Column,
    String,
    Numeric,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Invoice(Base):

    __tablename__ = "invoices"


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


    encounter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("encounters.id"),
        nullable=True
    )


    invoice_number = Column(
        String(100),
        nullable=False,
        unique=True
    )


    total_amount = Column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )


    amount_paid = Column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )


    status = Column(
        String(50),
        nullable=False,
        default="unpaid"
    )


    issued_at = Column(
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