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


class Medication(Base):

    __tablename__ = "medications"


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


    generic_name = Column(
        String(255),
        nullable=True
    )


    medication_code = Column(
        String(100),
        nullable=True
    )


    category = Column(
        String(100),
        nullable=True
    )


    dosage_form = Column(
        String(100),
        nullable=True
    )


    strength = Column(
        String(100),
        nullable=True
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