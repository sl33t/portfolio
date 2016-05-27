from django.core.files import File
from django.test import TestCase
from htmlvalidator.client import ValidatingClient

from RickyCatron.settings import BASE_DIR
from home.models import PortfolioItem


class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.client = ValidatingClient()


class HomePageTestCase(BaseTestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class BlogTestCase(BaseTestCase):
    def test_blog(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)


class PortfolioTestCase(BaseTestCase):
    def test_portfolio(self):
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)


class PortfolioItemTestCase(BaseTestCase):
    def test_portfolio_item_1_404(self):
        response = self.client.get("/portfolio/1/")
        self.assertEqual(response.status_code, 404)

    def test_portfolio_item_1_200(self):
        test_image_path = BASE_DIR + "/../home/static/images/logo.png"
        with open(test_image_path, "rb") as picture:
            django_picture = File(picture)
            portfolio_item = PortfolioItem(title="test",
                                           description="Test desc",
                                           main_image_url=django_picture,
                                           examples1=django_picture,
                                           examples2=django_picture,
                                           examples3=django_picture)
            portfolio_item.save()
        response = self.client.get("/portfolio/1/")
        self.assertEqual(response.status_code, 200)


class ContactTestCase(BaseTestCase):
    def test_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)


class SendMailTestCase(BaseTestCase):
    def test_send_mail(self):
        response = self.client.get("/send_mail/")
        self.assertEqual(response.status_code, 404)
