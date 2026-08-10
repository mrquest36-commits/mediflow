from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class ImagingOrder(Base):

    __tablename__ = "imaging_orders"
    
    encounter = relationship(
        "Encounter",
        back_populates="imaging_orders"
    )


    result = relationship(
        "ImagingResult",
        back_populates="imaging_order",
        uselist=False
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id"),
        nullable=False
    )


    encounter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("encounters.id"),
        nullable=False
    )


    ordered_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    imaging_type = Column(
        String(100),
        nullable=False
    )


    procedure_name = Column(
        String(255),
        nullable=False
    )


    body_part = Column(
        String(100),
        nullable=True
    )


    priority = Column(
        String(50),
        nullable=False,
        default="routine"
    )


    status = Column(
        String(50),
        nullable=False,
        default="ordered"
    )


    clinical_reason = Column(
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