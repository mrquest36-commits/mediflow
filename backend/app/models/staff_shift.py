from sqlalchemy import (
    Column,
    String,
    Date,
    Time,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class StaffShift(Base):

    __tablename__ = "staff_shifts"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    staff_profile_id = Column(
        UUID(as_uuid=True),
        ForeignKey("staff_profiles.id"),
        nullable=False
    )


    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )


    shift_date = Column(
        Date,
        nullable=False
    )


    start_time = Column(
        Time,
        nullable=False
    )


    end_time = Column(
        Time,
        nullable=False
    )


    shift_type = Column(
        String(50),
        nullable=False,
        default="regular"
    )


    status = Column(
        String(50),
        nullable=False,
        default="scheduled"
    )


    notes = Column(
        String(255),
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