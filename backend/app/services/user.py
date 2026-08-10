from sqlalchemy.orm import Session

from app.repositories import user as repository
from app.schemas.user import UserCreate



def create_user(
    db: Session,
    user: UserCreate
):

    return repository.create(
        db,
        user
    )



def get_users(
    db: Session
):

    return repository.get_all(
        db
    )