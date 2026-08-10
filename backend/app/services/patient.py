from sqlalchemy.orm import Session


from app.repositories import patient as repository

from app.schemas.patient import PatientCreate



def create_patient(
    db: Session,
    patient: PatientCreate
):

    return repository.create(
        db,
        patient
    )



def get_patients(
    db: Session
):

    return repository.get_all(
        db
    )



def get_patient(
    db: Session,
    patient_id
):

    return repository.get_by_id(
        db,
        patient_id
    )