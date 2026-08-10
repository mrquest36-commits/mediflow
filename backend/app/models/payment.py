from sqlalchemy import (
    Column,
    String,
    Text,
    Numeric,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Payment(Base):

    __tablename__ = "payments"


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


    invoice_id = Column(
        UUID(as_uuid=True),
        ForeignKey("invoices.id"),
        nullable=False
    )


    received_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    amount = Column(
        Numeric(12, 2),
        nullable=False
    )


    payment_method = Column(
        String(100),
        nullable=False
    )


    transaction_reference = Column(
        String(255),
        nullable=True
    )


    notes = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="completed"
    )


    paid_at = Column(
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