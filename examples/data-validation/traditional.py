from pydantic import BaseModel, field_validator
from typing import Optional

class UserInput(BaseModel):
    email: str
    age: Optional[int] = None
    phone: Optional[str] = None

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        # TODO: more rules? GDPR? audit logging?
        if '@' not in v:
            raise ValueError("Invalid email format")
        return v

    # TODO: add phone validation, PII handling, error messaging for users