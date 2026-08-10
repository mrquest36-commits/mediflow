from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class AppointmentCheckIn(Base):

    __tablename__ = "appointment_checkins"


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


    appointment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
        nullable=False
    )


    checked_in_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    check_in_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    queue_number = Column(
        String(50),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="waiting"
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