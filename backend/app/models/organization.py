from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.base import Base


class Organization(Base):

    __tablename__ = "organizations"


    users = relationship(
        "User",
        back_populates="organization"
    )


    patients = relationship(
        "Patient",
        back_populates="organization"
    )


    organization_units = relationship(
        "OrganizationUnit",
        back_populates="organization"
    )


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    name = Column(
        String(255),
        nullable=False
    )


    code = Column(
        String(20),
        unique=True,
        nullable=False
    )


    organization_type = Column(
        String(50),
        nullable=False
    )


    logo_url = Column(
        Text,
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


    address = Column(
        Text,
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