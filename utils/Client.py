from typing import Union

import allure
import requests

from utils.validate_resp import validate_response
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, ValidationError


class ClientApi:
    def __init__(self):
        self.base_url = 'https://api.dev.abra-market.com'
        self.session = self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self,
                method: str,
                url: str,
                json=None,
                headers: str = None):

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
