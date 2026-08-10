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


class ImagingResult(Base):

    __tablename__ = "imaging_results"

    imaging_order = relationship(
        "ImagingOrder",
        back_populates="result"
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


    imaging_order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("imaging_orders.id"),
        nullable=False
    )


    performed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    findings = Column(
        Text,
        nullable=True
    )


    impression = Column(
        Text,
        nullable=True
    )


    report_status = Column(
        String(50),
        nullable=False,
        default="draft"
    )


    verified_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )


    verified_at = Column(
        DateTime(timezone=True),
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