from pydantic import BaseModel


class LoginModel(BaseModel):
    email: str
    password: str

class LoginResponseModel(BaseModel):
    ok: str
    result: str

class RegisterModel(BaseModel):
    email: str
    password: str

class RegisterResponseModel(BaseModel):
    ok: str
    result: str