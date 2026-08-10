from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class PurchaseOrderItem(Base):

    __tablename__ = "purchase_order_items"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    purchase_order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("purchase_orders.id"),
        nullable=False
    )


    medication_id = Column(
        UUID(as_uuid=True),
        ForeignKey("medications.id"),
        nullable=True
    )


    item_name = Column(
        String(255),
        nullable=False
    )


    quantity_ordered = Column(
        Integer,
        nullable=False
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