from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class MedicationAdministration(Base):

    __tablename__ = "medication_administrations"


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


    prescription_id = Column(
        UUID(as_uuid=True),
        ForeignKey("prescriptions.id"),
        nullable=False
    )


    admission_id = Column(
        UUID(as_uuid=True),
        ForeignKey("admissions.id"),
        nullable=True
    )


    administered_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    dose_given = Column(
        String(100),
        nullable=False
    )


    route = Column(
        String(100),
        nullable=True
    )


    status = Column(
        String(50),
        nullable=False,
        default="administered"
    )


    notes = Column(
        Text,
        nullable=True
    )


    administered_at = Column(
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