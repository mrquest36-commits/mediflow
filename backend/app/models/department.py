from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Department(Base):

    __tablename__ = "departments"

    encounters = relationship(
    "Encounter",
    back_populates="department"
)

    wards = relationship(
        "Ward",
        back_populates="department"
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )


    name = Column(
        String(255),
        nullable=False
    )


    code = Column(
        String(50),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="active"
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