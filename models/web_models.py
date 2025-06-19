from typing import Optional, List, Union

from pydantic import BaseModel


class LoginModel(BaseModel):
    email: str
    password: Optional[str]

class LoginResponseModel(BaseModel):
    ok: bool
    result: bool

class RegisterModel(BaseModel):
    email: str
    password: Optional[str]

class RegisterResponseModel(BaseModel):
    ok: bool
    result: bool


class PersonalInfoUpdate(BaseModel):
    first_name: str
    last_name: str
    country_id: int
    phone_number: int

class PersonalInfoUpdateResponseModel(BaseModel):
    ok: bool
    result: bool
    # detail: str
    # error: str
    # error_code: 0

#Negative Models
class ErrorDetail(BaseModel):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]


class ValidationError(BaseModel):
    detail: Optional[list]=[ErrorDetail]