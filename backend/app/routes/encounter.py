from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.encounter import (
    EncounterCreate,
    EncounterResponse
)

from app.services import encounter as service


router = APIRouter(
    prefix="/encounters",
    tags=["Encounters"]
)


@router.post(
    "/",
    response_model=EncounterResponse
)
def create_encounter(
    encounter: EncounterCreate,
    db: Session = Depends(get_db)
):

    return service.create_encounter(
        db,
        encounter
    )


@router.get(
    "/",
    response_model=list[EncounterResponse]
)
def get_encounters(
    db: Session = Depends(get_db)
):

    return service.get_encounters(
        db
    )


@router.get(
    "/{encounter_id}",
    response_model=EncounterResponse
)
def get_encounter(
    encounter_id,
    db: Session = Depends(get_db)
):

    return service.get_encounter(
        db,
        encounter_id
    )

@router.get(
    "/patient/{patient_id}",
    response_model=list[EncounterResponse]
)
def get_patient_encounters(
    patient_id,
    db: Session = Depends(get_db)
):

    return service.get_patient_encounters(
        db,
        patient_id
    )