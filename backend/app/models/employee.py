from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Employee(Base):

    __tablename__ = "employees"


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


    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )


    employee_number = Column(
        String(50),
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


    employee_type = Column(
        String(50),
        nullable=False
    )


    specialization = Column(
        String(150),
        nullable=True
    )


    phone = Column(
        String(30),
        nullable=True
    )


    email = Column(
        String(255),
        nullable=True
    )


    is_active = Column(
        Boolean,
        default=True
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
    