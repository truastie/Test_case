
import allure
import requests

from validate_resp import validate_response
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel


class ClientApi:
    def __init__(self):
        self.base_url = 'https://dev.abra-market.com'
        self.session = self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self,
                method: str,
                url: str,
                json=None):

        response = self.session.request(
            method=method,
            url=self.base_url+url,
            json=json
        )
        return response

class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /login')
    def login(self,
              request:LoginModel,
              expected_model:LoginResponseModel,
              status_code: int = 200):
        response = self.request(
            method='POST',
            url='/auth/sign-in',
            json=request.model_dump()
        )
        validate_response(response=response, model=expected_model, status_code=status_code)
        return validate_response

    @allure.step('POST /register')
    def registration(self,
                     request: RegisterModel,
                     expected_model: RegisterResponseModel,
                     status_code: int = 200):
        response = self.request(
            method='POST',
            url='/auth/sign-up/supplier',
            json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)
