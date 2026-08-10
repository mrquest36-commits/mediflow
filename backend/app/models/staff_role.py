from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class StaffRole(Base):

    __tablename__ = "staff_roles"


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


    role_name = Column(
        String(100),
        nullable=False
    )


    description = Column(
        String(255),
        nullable=True
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


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )