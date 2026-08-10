from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class StaffProfile(Base):

    __tablename__ = "staff_profiles"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )


    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )


    first_name = Column(
        String(100),
        nullable=False
    )


    last_name = Column(
        String(100),
        nullable=False
    )


    employee_number = Column(
        String(100),
        nullable=False,
        unique=True
    )


    profession = Column(
        String(100),
        nullable=False
    )


    license_number = Column(
        String(100),
        nullable=True
    )


    phone = Column(
        String(50),
        nullable=True
    )


    email = Column(
        String(255),
        nullable=True
    )


    date_of_birth = Column(
        Date,
        nullable=True
    )


    employment_date = Column(
        Date,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="active"
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