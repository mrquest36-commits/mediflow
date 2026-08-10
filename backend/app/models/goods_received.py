from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class GoodsReceived(Base):

    __tablename__ = "goods_received"


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


    received_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    delivery_reference = Column(
        String(255),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="received"
    )


    notes = Column(
        Text,
        nullable=True
    )


    received_at = Column(
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