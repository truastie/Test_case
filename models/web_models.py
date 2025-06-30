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

class SellerAddressRequest(BaseModel):
    is_main: bool
    country_id: int
    first_name: str
    last_name: str
    city: str
    street: str
    building: str
    apartment: str
    postal_code: str

# Модель для телефонных данных
class SellerAddressPhoneRequest(BaseModel):
    country_id: int
    phone_number: str

# Обертка для всего тела запроса
class SellerAddressRequestBody(BaseModel):
    seller_address_request: SellerAddressRequest
    seller_address_phone_request: SellerAddressPhoneRequest

class SellerAddressRequestResponseModel(BaseModel):
    ok: bool

class AddingElementtoFavModel(BaseModel):
    product_id:int

class AddingElementtoFavResponseModel(BaseModel):
    ok: bool
    result: bool


class SupplierProductAddModel(BaseModel):
    name: str
    description: str
    brand: int
    category: int

class SupplierProductAddResponseModel(BaseModel):
    ok: bool


#Negative Models
class ErrorDetail(BaseModel):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]


class ValidationError(BaseModel):
    detail: Optional[list]=[ErrorDetail]