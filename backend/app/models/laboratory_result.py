from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class LaboratoryResult(Base):

    __tablename__ = "laboratory_results"

    laboratory_order = relationship(
        "LaboratoryOrder",
        back_populates="results"
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


    laboratory_order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("laboratory_orders.id"),
        nullable=False
    )


    result_name = Column(
        String(255),
        nullable=False
    )


    result_value = Column(
        String(255),
        nullable=False
    )


    unit = Column(
        String(50),
        nullable=True
    )


    reference_range = Column(
        String(100),
        nullable=True
    )


    is_abnormal = Column(
        Boolean,
        default=False
    )


    interpretation = Column(
        Text,
        nullable=True
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