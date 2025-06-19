import random
import string
import json

# class TempMail:
#     def __init__(self):
#         self.email = self.random_email()
#         self.messages = []

def random_name()->str:
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(10)])

def random_digits_name(length=11):
    return ''.join([random.choice(string.digits) for _ in range(length)])

def random_email():
    return random_name() + '@gmail.com'


def random_password():
    return random_name() + '!' + ''.join([random.choice(string.digits) for i in range(4)])