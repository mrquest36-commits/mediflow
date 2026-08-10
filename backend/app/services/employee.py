from sqlalchemy.orm import Session

from app.repositories import employee as repository
from app.schemas.employee import EmployeeCreate


def create_employee(
    db: Session,
    employee: EmployeeCreate
):

    return repository.create(
        db,
        employee
    )


def get_employees(
    db: Session
):

    return repository.get_all(
        db
    )