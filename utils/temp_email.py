import requests
import string
import random

MAIL_TM_BASE = "https://api.mail.tm"


def create_temp_email():
    local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain_resp = requests.get(f"{MAIL_TM_BASE}/domains")
    if domain_resp.status_code != 200:
        raise Exception(f"Ошибка получения домена: {domain_resp.status_code} {domain_resp.text}")
    domains = domain_resp.json().get("hydra:member", [])
    if not domains:
        raise Exception("Не получены домены с mail.tm")

    domain = domains[0]["domain"]
    email = f"{local}@{domain}"
    password = "StrongP@ssword123"

    # Создаём аккаунт
    account_data = {"address": email, "password": password}
    create_resp = requests.post(f"{MAIL_TM_BASE}/accounts", json=account_data)
    if create_resp.status_code not in (200, 201):
        raise Exception(f"Ошибка при создании почты: {create_resp.status_code} {create_resp.text}")

    # Получаем токен
    token_resp = requests.post(f"{MAIL_TM_BASE}/token", json=account_data)
    if token_resp.status_code != 200:
        raise Exception(f"Ошибка получения токена: {token_resp.status_code} {token_resp.text}")

    token = token_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    return email, headers

def get_messages(headers):
    response = requests.get(f"{MAIL_TM_BASE}/messages", headers=headers)
    if response.status_code != 200:
        raise requests.HTTPError(f"Ошибка API: {response.status_code} {response.text}")
    return response.json()["hydra:member"]


def read_message(message_id, headers):
    response = requests.get(f"{MAIL_TM_BASE}/messages/{message_id}", headers=headers)
    if response.status_code != 200:
        raise requests.HTTPError(f"Ошибка API: {response.status_code} {response.text}")
    return response.json()