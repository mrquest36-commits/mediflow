from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Service(Base):

    __tablename__ = "services"


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


    organization_unit_id = Column(
        UUID(as_uuid=True),
        ForeignKey("organization_units.id"),
        nullable=True
    )


    name = Column(
        String(255),
        nullable=False
    )


    code = Column(
        String(50),
        nullable=False
    )


    service_type = Column(
        String(100),
        nullable=False
    )


    description = Column(
        Text,
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