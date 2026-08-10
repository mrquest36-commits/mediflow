from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services import user as service



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
    db: Session = Depends(get_db)
):

    return service.get_users(
        db
    )