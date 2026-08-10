from sqlalchemy import (
    Column,
    String,
    Text,
    Numeric,
    DateTime,
    Date,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class EquipmentRepair(Base):

    __tablename__ = "equipment_repairs"


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


    reported_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    repaired_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )


    problem_description = Column(
        Text,
        nullable=False
    )


    repair_description = Column(
        Text,
        nullable=True
    )


    repair_date = Column(
        Date,
        nullable=True
    )


    repair_cost = Column(
        Numeric(12, 2),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="reported"
    )


    notes = Column(
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