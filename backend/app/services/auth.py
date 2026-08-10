from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from app.repositories import user as user_repository
from app.schemas.auth import LoginRequest
from app.core.security import (
    verify_password,
    create_access_token
)


def login(
    db: Session,
    credentials: LoginRequest
):

    user = user_repository.get_by_email(
        db,
        credentials.email
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not user.is_active:

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    password_valid = verify_password(
        credentials.password,
        user.password_hash
    )

    if not password_valid:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token({
        "sub": str(user.id),
        "organization_id": str(
            user.organization_id
        )
    })

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "organization_id": user.organization_id,
        "first_name": user.first_name,
        "last_name": user.last_name
    }