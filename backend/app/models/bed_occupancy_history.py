from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class BedOccupancyHistory(Base):

    __tablename__ = "bed_occupancy_histories"

    bed = relationship(
        "Bed",
        back_populates="occupancy_history"
    )


    admission = relationship(
        "Admission",
        back_populates="occupancy_history"
    )


    bed_assignment = relationship(
        "BedAssignment",
        back_populates="occupancy_history"
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


    bed_id = Column(
        UUID(as_uuid=True),
        ForeignKey("beds.id"),
        nullable=False
    )


    admission_id = Column(
        UUID(as_uuid=True),
        ForeignKey("admissions.id"),
        nullable=False
    )


    bed_assignment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("bed_assignments.id"),
        nullable=False
    )


    event_type = Column(
        String(50),
        nullable=False
    )


    occupied_from = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    occupied_until = Column(
        DateTime(timezone=True),
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )