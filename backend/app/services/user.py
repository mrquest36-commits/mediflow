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



from uuid import UUID

def get_users(
    db: Session,
    organization_id: UUID
):
    return repository.get_all(
        db,
        organization_id
    )