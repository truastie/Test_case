import json
from typing import Union

import allure
import requests

from utils.validate_resp import validate_response
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, ValidationError, \
    PersonalInfoUpdate, PersonalInfoUpdateResponseModel, SellerAddressRequestResponseModel, \
    SellerAddressRequestBody, AddingElementtoFavModel, AddingElementtoFavResponseModel, SupplierProductAddModel, \
    SupplierProductAddResponseModel, SupplierUpdateNotification, SupplierNotificationResponseModel, \
    ApplicationResponseBoolModel, ApplicationResponseCompanyModel, ResetPasswordRequest, ForgotPasswordResponse, \
    RemoveElementfromFav,DeleteSellerAddressResponse


class ClientApi:
    def __init__(self):
        self.base_url = 'https://api.dev.abra-market.com'
        self.session = self._initialize_session()
        self.auth_token = None

    def set_token(self, token):
        self.auth_token = token

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self,
                method: str,
                url: str,
                data=None,
                params=None,
                files=None,
                json=None):
        headers = {}
        if self.auth_token:
            # добавляем токен в headers, если есть
            headers['Authorization'] = f'Bearer {self.auth_token}'
        response = self.session.request(
            method=method,
            url=self.base_url+url,
            data=data,
            params=params,
            files=files,
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

    def delete_sellers_address(self,
                               expected_model:DeleteSellerAddressResponse,
                               address_id,
                               status_code=200):

        response=self.request(
            method='DELETE',
            url=f'/sellers/addresses/{address_id}/remove'
        )

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

    @allure.step('DELETE / remove product from favorites seller')
    def delete_element_from_favorites(self,
                                      request:RemoveElementfromFav,
                                      expected_model:AddingElementtoFavResponseModel,
                                      status_code: int=200):
        response = self.request(
            method='DELETE',
            url='/sellers/favorites/remove',
            params={'product_id': request.product_id}
        )

        print(response)
        return validate_response(response=response, model=expected_model, status_code=status_code)

    def post_supplier_add_product(self,
                                  request:SupplierProductAddModel,
                                  expected_model:SupplierProductAddResponseModel,
                                  status_code: int=200):

        # response = self.request(
        #     method='POST',
        #     url='/suppliers/products/add',
        #     json=request.model_dump())
        #
        # return validate_response(response=response, model=expected_model, status_code=status_code)
        files = {}
        data = {
            'name': request.name,
            'description': request.description,
            'brand': str(request.brand),
            'category': str(request.category),
        }
        if request.image_path:
            with open(request.image_path, 'rb') as img:
                files['image'] = (
                request.image_path.split("\\")[-1], img, 'pic.png')
                response = self.request(
                    method='POST',
                    url='/suppliers/products/add',
                    data=data,
                    files=files
                )
        else:
            response = self.request(
                method='POST',
                url='/suppliers/products/add',
                data=data
            )
        return validate_response(response=response, model=expected_model, status_code=status_code)



    def post_supplier_notification(self,
                                   request:SupplierUpdateNotification,
                                   expected_model:SupplierNotificationResponseModel,
                                   status_code: int=200):
        payload = json.loads(request.model_dump_json())
        print("Sending body:", json.dumps(payload))
        response = self.request(
            method='POST',
            url='/suppliers/notifications/update',
            json=payload
        )
        print("API answer:", response.text)
        return validate_response(response=response, model=expected_model, status_code=status_code)

    def get_company_id(self,
                       company_id,
                       expected_model: ApplicationResponseCompanyModel,
                       status_code):
        response = self.request(
            method='get',
            url=f'/companies/{company_id}/info'
        )
        return validate_response(response=response, model=expected_model, status_code=status_code)


    @allure.step('DELETE /delete')
    def delete_account(self,
                       expected_model: ApplicationResponseBoolModel,
                       status_code):
        response = self.request(
            method='delete',
            url='users/account/delete'
        )
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /users/password/forgot')
    def forgot_password(self,
                        email: str,
                        expected_model,
                        status_code=200):
        response = self.request(
            method='post',
            url=f'/users/password/forgot?email={email}')
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /users/password/reset')
    def reset_password(self, token: str,
                       request: ResetPasswordRequest,
                       expected_model: ForgotPasswordResponse,
                       status_code=200):
        response = self.request(
            method='post',
            url=f'/users/password/reset?token={token}',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)