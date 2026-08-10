from sqlalchemy.orm import Session


from app.models.patient import Patient

from app.schemas.patient import PatientCreate



def create(
    db: Session,
    patient: PatientCreate
):

    db_patient = Patient(
        **patient.model_dump()
    )


    db.add(db_patient)

    db.commit()

    db.refresh(db_patient)


    return db_patient



def get_all(
    db: Session
):

    return db.query(
        Patient
    ).all()



def get_by_id(
    db: Session,
    patient_id
):

    return db.query(
        Patient
    ).filter(
        Patient.id == patient_id
    ).first()