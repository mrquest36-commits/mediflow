from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate



def create(
    db: Session,
    organization: OrganizationCreate
):

    db_organization = Organization(
        **organization.model_dump()
    )

    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)

    return db_organization



def get_all(db: Session):

    return db.query(
        Organization
    ).all()