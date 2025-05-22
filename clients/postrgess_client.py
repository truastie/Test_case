import psycopg2
import pytest

from models.postgress_model import UserModel
from utils import generator
from utils.common_checker import check_difference_between_objects
from utils.generator import random_email


class PostgresClient:

    @staticmethod
    def get_instance(request: str):
        connection = psycopg2.connect(database='postgres', user='test_user', password='postgres',
                                      host='172.212.108.64', port=6532)
        cursor = connection.cursor()
        cursor.execute(request)
        return cursor.fetchall()

    def get_user(self, email: str, is_deleted: bool, is_verified: bool):
        results = self.get_instance('select * from "user" u where email = '
                          f"'{email}'")
        assert len(results) == 1
        actual_model = UserModel(email=results[0][3], is_deleted=results[0][1], is_verified=results[0][0])
        expected_model = UserModel(email=email, is_deleted=is_deleted, is_verified=is_verified)
        check_difference_between_objects(actual_model, expected_model)

    def user_registration(self, email:str, is_deleted: bool, is_verified: bool):
        results = self.get_instance('select * from "user" u where email = '
                                    f"'{email}'")
        assert len(results) == 1
        email = generator.random_email()
        actual_model = UserModel(email=email, is_deleted=results[0][1], is_verified=results[0][0])
        expected_model = UserModel(email=email, is_deleted=False, is_verified=False)
        check_difference_between_objects(actual_model, expected_model)