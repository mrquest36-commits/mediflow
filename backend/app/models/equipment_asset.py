from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class EquipmentAsset(Base):

    __tablename__ = "equipment_assets"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    equipment_category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("equipment_categories.id"),
        nullable=False
    )


    name = Column(
        String(255),
        nullable=False
    )


    asset_code = Column(
        String(100),
        nullable=False,
        unique=True
    )


    serial_number = Column(
        String(255),
        nullable=True
    )


    manufacturer = Column(
        String(255),
        nullable=True
    )


    model_number = Column(
        String(255),
        nullable=True
    )


    location = Column(
        String(255),
        nullable=True
    )


    purchase_date = Column(
        Date,
        nullable=True
    )


    warranty_expiry = Column(
        Date,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="operational"
    )


    description = Column(
        Text,
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
    