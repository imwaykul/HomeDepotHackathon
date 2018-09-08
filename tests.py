from flask import Flask
from flask_testing import TestCase, LiveServerTestCase
import unittest
from urllib.request import urlopen

class TestAppCreatedProperly(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_create_app(self):
        assert self.client != None

class ServerRunsOnStart(LiveServerTestCase):

    def create_app(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        return self.app

    def test_server_runs_on_start(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.code, 200)     

if __name__ == '__main__':
    unittest.main()