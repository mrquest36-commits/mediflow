from sqlalchemy import Column, String, Text

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.models.base import Base


class Permission(Base):

    __tablename__ = "permissions"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    name = Column(
        String(100),
        unique=True,
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )