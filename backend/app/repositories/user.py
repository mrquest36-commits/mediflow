from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

from app.core.security import hash_password



def create(
    db: Session,
    user: UserCreate
):

    db_user = User(
        organization_id=user.organization_id,
        employee_id=user.employee_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )


    db.add(db_user)

    db.commit()

    db.refresh(db_user)


    return db_user



def get_all(
    db: Session
):

    return db.query(
        User
    ).all()

def get_by_email(
    db: Session,
    email: str
):

    return db.query(
        User
    ).filter(
        User.email == email
    ).first()