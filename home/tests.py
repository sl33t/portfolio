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

    def test_blog(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_portfolio(self):
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)

    def test_portfolio_item(self):
        response = self.client.get("/portfolio/1/")
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_send_mail(self):
        response = self.client.get("/send_mail/")
        self.assertEqual(response.status_code, 404)
