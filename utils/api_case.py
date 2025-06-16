import json
import re

import requests

from utils import generator


class WebApi:
    def __init__(self):
        self.base_url='https://dev.abra-market.com'


    def login(self, request) -> json:
        response = requests.post(self.base_url + '/auth/sign-in', data=json.dumps(request))
        return response.json(), response.status_code

    def registration(self, request) -> json:
        response = requests.post(self.base_url + '/auth/sign-up/supplier', data=json.dumps(request))
        return response.json(), response.status_code
#