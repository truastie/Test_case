from typing import Union

import allure
import requests

from utils.validate_resp import validate_response
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, ValidationError, \
    PersonalInfoUpdate, PersonalInfoUpdateResponseModel, SellerAddressRequestResponseModel, \
    SellerAddressRequestBody, AddingElementtoFavModel, AddingElementtoFavResponseModel, SupplierProductAddModel, \
    SupplierProductAddResponseModel, SupplierUpdateNotification, SupplierNotificationResponseModel


class ClientApi:
    def __init__(self):
        self.base_url = 'https://api.dev.abra-market.com'
        self.session = self._initialize_session()
        self.auth_token = None

    # def set_token(self, token):
    #     self.auth_token = token

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self,
                method: str,
                url: str,
                json=None):
        headers = {}
        if self.auth_token:
            # добавляем токен в headers, если есть
            headers['Authorization'] = f'Bearer {self.auth_token}'
        response = self.session.request(
            method=method,
            url=self.base_url+url,
            headers=headers,
            json=json
        )
        return response

class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /login')
    def login(self,
              request:LoginModel,
              expected_model: Union[LoginResponseModel,ValidationError],
              status_code: int = 200):
        response = self.request(
            method='POST',
            url='/auth/sign-in',
            json=request.model_dump()
        )
        # token = response.json().get("token")
        # print(f"Полученный токен: {token}")
        # assert token, "Token не получен при логине"  # проверка
        # self.auth_token = token
        # return validate_response(response=response, model=expected_model, status_code=status_code)
        print("Ответ при логине:", response.text)
        try:
            print("Ответ json:", response.json())
        except Exception:
            print("Не удалось распарсить JSON")
        token = response.json().get("token")
        print(f"Полученный токен: {token}")
        assert token, "Token не получен при логине"
        self.auth_token = token
        return validate_response(response=response, model=expected_model, status_code=status_code)


    @allure.step('POST /register')
    def registration(self,
                     request: RegisterModel,
                     expected_model: RegisterResponseModel,
                     user_type: str,
                     status_code: int = 200):
        response = self.request(
            method='POST',
            url=f'/auth/sign-up/{user_type}',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /personalInfo Update')
    def post_info_update(self,
                            request:PersonalInfoUpdate,
                            expected_model: PersonalInfoUpdateResponseModel,
                            status_code: int = 200):
        response = self.request(
            method='POST',
            url=f'/users/account/personalInfo/update',
            json = request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /sellers/addresses/add')
    def post_sellers_adding_address(self,
                                    request:SellerAddressRequestBody,
                                    expected_model:SellerAddressRequestResponseModel,
                                    status_code: int = 201):
        response = self.request(
            method='POST',
            url='/sellers/addresses/add',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)

    def post_adding_element_to_fav(self,
                                   request:AddingElementtoFavModel,
                                   expected_model:AddingElementtoFavResponseModel,
                                   status_code: int=200):
        response = self.request(
            method='POST',
            url='/sellers/favorites/add',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)

    def post_supplier_add_product(self,
                                  request:SupplierProductAddModel,
                                  expected_model:SupplierProductAddResponseModel,
                                  status_code: int=200):

        response = self.request(
            method='POST',
            url='/suppliers/products/add',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)


    def post_supplier_notification(self,
                                   request=SupplierUpdateNotification,
                                   expected_model=SupplierNotificationResponseModel,
                                   status_code=200):
        response = self.request(
            method='POST',
            url='/suppliers/notifications/update',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)