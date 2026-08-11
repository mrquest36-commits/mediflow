from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services import user as service
from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return service.create_user(
        db,
        user
    )


@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.get_users(
        db,
        current_user.organization_id
    )
