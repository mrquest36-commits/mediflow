from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Procedure(Base):

    __tablename__ = "procedures"

    encounter = relationship(
        "Encounter",
        back_populates="procedures"
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


    encounter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("encounters.id"),
        nullable=False
    )


    performed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    procedure_name = Column(
        String(255),
        nullable=False
    )


    procedure_type = Column(
        String(100),
        nullable=False
    )

    procedure_category = Column(
        String(100),
        nullable=False
    )


    requires_theatre = Column(
        Boolean,
        nullable=False,
        default=False
    )

    description = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="completed"
    )


    performed_at = Column(
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