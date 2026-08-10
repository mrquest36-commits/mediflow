from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class User(Base):

    __tablename__ = "users"

    encounters = relationship(
        "Encounter",
        back_populates="recorded_user"
    )
    
    organization = relationship(
        "Organization",
        back_populates="users"
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


    employee_id = Column(
        String(50),
        unique=True,
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


    email = Column(
        String(255),
        unique=True,
        nullable=False
    )


    password_hash = Column(
        String(255),
        nullable=False
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