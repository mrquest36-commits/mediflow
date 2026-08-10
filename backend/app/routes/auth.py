from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.auth import (
    LoginRequest,
    LoginResponse
)

from app.services import auth as service


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    return service.login(
        db,
        credentials
    )