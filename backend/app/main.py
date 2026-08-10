from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routes import organization
from app.routes import user
from app.routes import auth
from app.routes import employee
from app.routes import patient
from app.routes import encounter




app = FastAPI(
    title="MediFlow API",
    version="1.0.0",
)


app.include_router(
    organization.router
)


app.include_router(
    user.router
)

app.include_router(
    auth.router
)

app.include_router(
    employee.router
)

app.include_router(
    patient.router
)

app.include_router(
    encounter.router
)






@app.get("/")
def root():
    return {
        "message": "MediFlow API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "MediFlow API",
        "version": app.version,
    }


@app.get("/database-check") 
def database_check():

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT current_database();")
            )

            database = result.fetchone()[0]


        return {
            "status": "connected",
            "database": database,
        }


    except Exception as error:

        return {
            "status": "failed",
            "error": str(error),
        }