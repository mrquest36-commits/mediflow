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


class PurchaseOrder(Base):

    __tablename__ = "purchase_orders"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    supplier_id = Column(
        UUID(as_uuid=True),
        ForeignKey("suppliers.id"),
        nullable=False
    )


    ordered_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    purchase_order_number = Column(
        String(100),
        nullable=False,
        unique=True
    )


    total_amount = Column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )


    status = Column(
        String(50),
        nullable=False,
        default="pending"
    )


    notes = Column(
        Text,
        nullable=True
    )


    ordered_at = Column(
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