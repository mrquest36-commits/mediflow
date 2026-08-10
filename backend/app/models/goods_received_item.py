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


class GoodsReceivedItem(Base):

    __tablename__ = "goods_received_items"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    goods_received_id = Column(
        UUID(as_uuid=True),
        ForeignKey("goods_received.id"),
        nullable=False
    )


    purchase_order_item_id = Column(
        UUID(as_uuid=True),
        ForeignKey("purchase_order_items.id"),
        nullable=True
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


    quantity_received = Column(
        Integer,
        nullable=False
    )


    unit_cost = Column(
        Numeric(12, 2),
        nullable=True
    )


    batch_number = Column(
        String(100),
        nullable=True
    )


    expiry_date = Column(
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