from sqlalchemy import (
    Column,
    String,
    Text,
    Numeric,
    Integer,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class InvoiceItem(Base):

    __tablename__ = "invoice_items"


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


    item_type = Column(
        String(100),
        nullable=False
    )


    item_name = Column(
        String(255),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )


    unit_price = Column(
        Numeric(12, 2),
        nullable=False
    )


    total_price = Column(
        Numeric(12, 2),
        nullable=False
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