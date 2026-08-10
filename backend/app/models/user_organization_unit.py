from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from app.models.base import Base


class UserOrganizationUnit(Base):

    __tablename__ = "user_organization_units"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )


    organization_unit_id = Column(
        UUID(as_uuid=True),
        ForeignKey("organization_units.id"),
        nullable=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )