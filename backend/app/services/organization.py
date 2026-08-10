from sqlalchemy.orm import Session

from app.repositories import organization as repository
from app.schemas.organization import OrganizationCreate



def create_organization(
    db: Session,
    organization: OrganizationCreate
):

    return repository.create(
        db,
        organization
    )



def get_organizations(
    db: Session
):

    return repository.get_all(db)