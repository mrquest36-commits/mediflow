from sqlalchemy.orm import Session

from app.repositories import encounter as repository

from app.schemas.encounter import EncounterCreate


def create_encounter(
    db: Session,
    encounter: EncounterCreate
):

    return repository.create(
        db,
        encounter
    )


def get_encounters(
    db: Session
):

    return repository.get_all(
        db
    )


def get_encounter(
    db: Session,
    encounter_id
):

    return repository.get_by_id(
        db,
        encounter_id
    )


def get_patient_encounters(
    db: Session,
    patient_id
):

    return repository.get_by_patient(
        db,
        patient_id
    )