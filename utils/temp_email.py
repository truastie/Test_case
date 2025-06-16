import requests

import requests
from requests.adapters import HTTPAdapter, Retry

def get_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session

session = get_session()

def generate_random_email():
    import random
    import string
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{login}@1secmail.com"
    return login, email

def get_messages(login):
    url = f"https://api.1secmail.com/?action=getMessages&login={login}&domain=1secmail.com"
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def read_message(login, message_id):
    url = f"https://api.1secmail.com/?action=readMessage&login={login}&domain=1secmail.com&id={message_id}"
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
