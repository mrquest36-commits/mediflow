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


class Dispensation(Base):

    __tablename__ = "dispensations"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    prescription_id = Column(
        UUID(as_uuid=True),
        ForeignKey("prescriptions.id"),
        nullable=False
    )


    medication_id = Column(
        UUID(as_uuid=True),
        ForeignKey("medications.id"),
        nullable=False
    )


    inventory_stock_id = Column(
        UUID(as_uuid=True),
        ForeignKey("inventory_stocks.id"),
        nullable=False
    )


    dispensed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    quantity_dispensed = Column(
        Integer,
        nullable=False
    )


    status = Column(
        String(50),
        nullable=False,
        default="dispensed"
    )


    notes = Column(
        Text,
        nullable=True
    )


    dispensed_at = Column(
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