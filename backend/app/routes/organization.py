from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse
)

from app.services import organization as service


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)





@router.post(
    "/",
    response_model=OrganizationResponse
)
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):

    return service.create_organization(
        db,
        organization
    )



@router.get(
    "/",
    response_model=list[OrganizationResponse]
)
def get_organizations(
    db: Session = Depends(get_db)
):

    return service.get_organizations(
        db
    )