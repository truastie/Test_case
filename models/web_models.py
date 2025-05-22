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


#Negative Models
class ErrorDetail(BaseModel):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]


class ValidationError(BaseModel):
    detail: Optional[list]=[ErrorDetail]