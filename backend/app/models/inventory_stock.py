from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class InventoryStock(Base):

    __tablename__ = "inventory_stocks"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    medication_id = Column(
        UUID(as_uuid=True),
        ForeignKey("medications.id"),
        nullable=False
    )


    batch_number = Column(
        String(100),
        nullable=True
    )


    quantity = Column(
        Integer,
        nullable=False,
        default=0
    )


    reorder_level = Column(
        Integer,
        nullable=True
    )


    expiry_date = Column(
        DateTime(timezone=True),
        nullable=True
    )


    storage_location = Column(
        String(255),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="available"
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