from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    Date,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class EquipmentMaintenance(Base):

    __tablename__ = "equipment_maintenances"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    equipment_asset_id = Column(
        UUID(as_uuid=True),
        ForeignKey("equipment_assets.id"),
        nullable=False
    )


    performed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    maintenance_type = Column(
        String(100),
        nullable=False
    )


    scheduled_date = Column(
        Date,
        nullable=True
    )


    completed_date = Column(
        Date,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="scheduled"
    )


    notes = Column(
        Text,
        nullable=True
    )


    next_maintenance_date = Column(
        Date,
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