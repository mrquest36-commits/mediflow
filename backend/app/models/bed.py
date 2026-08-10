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


class Bed(Base):

    __tablename__ = "beds"

    ward = relationship(
        "Ward",
        back_populates="beds"
    )


    assignments = relationship(
        "BedAssignment",
        back_populates="bed"
    )

    occupancy_history = relationship(
        "BedOccupancyHistory",
        back_populates="bed"
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


    ward_id = Column(
        UUID(as_uuid=True),
        ForeignKey("wards.id"),
        nullable=False
    )


    bed_number = Column(
        String(100),
        nullable=False
    )

    bed_code = Column(
        String(100),
        nullable=False,
        unique=True
    )

    bed_type = Column(
        String(100),
        nullable=False
    )


    status = Column(
        String(50),
        nullable=False,
        default="available"
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