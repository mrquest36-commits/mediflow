from pydantic import BaseModel
from uuid import UUID


class LoginRequest(BaseModel):

    email: str
    password: str


class LoginResponse(BaseModel):

    access_token: str
    token_type: str

    user_id: UUID
    organization_id: UUID

    first_name: str
    last_name: str