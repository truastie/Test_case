from typing import Optional, List, Union
from datetime import datetime
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
    first_name: Optional[str]
    last_name: Optional[str]
    city: Optional[str]
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

class SellerAddressResultModel(BaseModel):
    id: int


class DeleteSellerAddressResponse(BaseModel):
    ok: bool
    result: bool

class SellerAddressRequestResponseModel(BaseModel):
    ok: bool
    result: SellerAddressResultModel

class AddingElementtoFavModel(BaseModel):
    product_id:int

class AddingElementtoFavResponseModel(BaseModel):
    ok: bool
    result: bool
class RemoveElementfromFav(BaseModel):
    product_id:int

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


class SupplierUpdateNotification(BaseModel):
    on_advertising_campaigns: bool
    on_order_updates: bool
    on_order_reminders: bool
    on_product_updates: bool
    on_product_reminders: bool
    on_reviews_of_products: bool
    on_change_in_demand: bool
    on_advice_from_abra: bool
    on_account_support: bool

class SupplierNotificationResponseModel(BaseModel):
    ok: bool
    result: bool

class ApplicationResponseBoolModel(BaseModel):
    ok: bool
    result: Optional[bool] = None
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

class Company(BaseModel):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: str
    year_established: int
    employees_number_id: int

class ApplicationResponseCompanyModel(BaseModel):
    ok: bool
    result: Optional[Company] = None
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

class ForgotPasswordResponse(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True
    # detail: Optional[str]
    # error: Optional[str]
    error_code: Optional[int] = 0

class ResetPasswordRequest(BaseModel):
    new_password: Optional[str]
    confirm_password: Optional[str]