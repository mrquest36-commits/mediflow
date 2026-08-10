from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


def create(
    db: Session,
    employee: EmployeeCreate
):

    db_employee = Employee(
        **employee.model_dump()
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_all(
    db: Session
):

    return db.query(
        Employee
    ).all()