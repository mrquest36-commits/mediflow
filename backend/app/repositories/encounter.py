from sqlalchemy.orm import Session

from app.models.encounter import Encounter

from app.schemas.encounter import EncounterCreate


def create(
    db: Session,
    encounter: EncounterCreate
):

    db_encounter = Encounter(
        **encounter.model_dump()
    )

    db.add(db_encounter)

    db.commit()

    db.refresh(db_encounter)

    return db_encounter


def get_all(
    db: Session
):

    return db.query(
        Encounter
    ).all()


def get_by_id(
    db: Session,
    encounter_id
):

    return db.query(
        Encounter
    ).filter(
        Encounter.id == encounter_id
    ).first()


def get_by_patient(
    db: Session,
    patient_id
):

    return db.query(
        Encounter
    ).filter(
        Encounter.patient_id == patient_id
    ).all()