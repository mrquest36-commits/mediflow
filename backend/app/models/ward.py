from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class Ward(Base):

    __tablename__ = "wards"

    admissions = relationship(
        "Admission",
        back_populates="ward"
    )


    department = relationship(
        "Department",
        back_populates="wards"
    )

    beds = relationship(
        "Bed",
        back_populates="ward"
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

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=True
    )

    name = Column(
        String(255),
        nullable=False
    )


    ward_type = Column(
        String(100),
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    capacity = Column(
        Integer,
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

    code = Column(
        String(50),
        nullable=False
    )