from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Supplier(Base):

    __tablename__ = "suppliers"


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


    supplier_code = Column(
        String(100),
        nullable=True
    )


    contact_person = Column(
        String(255),
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


    address = Column(
        Text,
        nullable=True
    )


    supplier_type = Column(
        String(100),
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