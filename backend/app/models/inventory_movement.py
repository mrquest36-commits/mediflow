from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class InventoryMovement(Base):

    __tablename__ = "inventory_movements"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    inventory_stock_id = Column(
        UUID(as_uuid=True),
        ForeignKey("inventory_stocks.id"),
        nullable=False
    )


    performed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    movement_type = Column(
        String(100),
        nullable=False
    )


    quantity = Column(
        Integer,
        nullable=False
    )


    reference_type = Column(
        String(100),
        nullable=True
    )


    reference_id = Column(
        UUID(as_uuid=True),
        nullable=True
    )


    notes = Column(
        Text,
        nullable=True
    )


    performed_at = Column(
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