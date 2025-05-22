from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    email: Optional[str] = None
    is_deleted: Optional[bool] = None
    is_verified: Optional[bool] = None