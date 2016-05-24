# Create your tests here.
from django.test import TestCase
from htmlvalidator.client import ValidatingClient


class MyAppTests(TestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.client = ValidatingClient()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
