from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base




class OrganizationUnit(Base):

    __tablename__ = "organization_units"


    organization = relationship(
        "Organization",
        back_populates="organization_units"
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


    name = Column(
        String(255),
        nullable=False
    )


    code = Column(
        String(50),
        nullable=False
    )


    unit_type = Column(
        String(50),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    parent_unit_id = Column(
        UUID(as_uuid=True),
        ForeignKey("organization_units.id"),
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