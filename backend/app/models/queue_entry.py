from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class QueueEntry(Base):

    __tablename__ = "queue_entries"


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


    patient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("patients.id"),
        nullable=False
    )


    appointment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
        nullable=True
    )


    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )


    queue_type = Column(
        String(100),
        nullable=False
    )


    queue_number = Column(
        Integer,
        nullable=False
    )


    priority = Column(
        String(50),
        nullable=False,
        default="normal"
    )


    status = Column(
        String(50),
        nullable=False,
        default="waiting"
    )


    called_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    completed_at = Column(
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