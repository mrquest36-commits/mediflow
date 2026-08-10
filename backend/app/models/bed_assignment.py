from sqlalchemy import (
    Column,
    DateTime,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class BedAssignment(Base):

    __tablename__ = "bed_assignments"

    admission = relationship(
        "Admission",
        back_populates="bed_assignments"
    )


    bed = relationship(
        "Bed",
        back_populates="assignments"
    )

    occupancy_history = relationship(
        "BedOccupancyHistory",
        back_populates="bed_assignment"
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


    admission_id = Column(
        UUID(as_uuid=True),
        ForeignKey("admissions.id"),
        nullable=False
    )


    bed_id = Column(
        UUID(as_uuid=True),
        ForeignKey("beds.id"),
        nullable=False
    )


    assigned_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    status = Column(
        String(50),
        nullable=False,
        default="active"
    )


    assigned_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    released_at = Column(
        DateTime(timezone=True),
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