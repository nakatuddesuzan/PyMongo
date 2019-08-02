import unittest

from flask import json

from app import app, app_config
from app.api.mongo import mongo

db = mongo.db


class BaseTest(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app
    
    def setUp(self):
        self.client = app.test_client(self)
    
    def tearDown(self):
        """
        Method to droP tables after the test is run
        """
        db.users.drop()
    
    def create_users(self, name, age):
        return self.client.post(
            '/users',
            data=json.dumps(dict(
                name = name,
                age = age

            )),
            content_type = 'application/json'
        )
    
    def get_all_users(self):
        return self.client.get(
            '/users',
        )
    
    def get_one_user(self, name):
        return self.client.get('/users/name')

class TestUsers(BaseTest):

    def test_create_users(self):
        """
            Test for successful user signup
        """
        with self.client:
            response = self.create_users("Suzan", "23")
            self.assertEqual(response.status_code, 200)
    
    def test_get_all_users(self):
        """
            Test for succesful retrieving of users
        """
        with self.client:
            response = self.get_all_users()
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
    
    def test_get_one_user(self):
        """
            Test for succesful retrieving of one user
        """
        with self.client:
            response = self.get_one_user("suzan")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)

