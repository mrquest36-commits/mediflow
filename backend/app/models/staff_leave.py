from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    Integer,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class StaffLeave(Base):

    __tablename__ = "staff_leaves"


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


    leave_type = Column(
        String(100),
        nullable=False
    )


    start_date = Column(
        Date,
        nullable=False
    )


    end_date = Column(
        Date,
        nullable=False
    )


    total_days = Column(
        Integer,
        nullable=False
    )


    reason = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="pending"
    )


    approved_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )


    approved_at = Column(
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