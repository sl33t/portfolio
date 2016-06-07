from django.core.files import File
from django.test import TestCase
from htmlvalidator.client import ValidatingClient

from RickyCatron.settings import BASE_DIR
from home.models import PortfolioItem, BlogPost


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


class BlogItemTestCase(BaseTestCase):

    def test_blog_item_1_404(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 404)

    def test_blog_item_1(self):
        test_image_path = BASE_DIR + "/../home/static/images/logo.png"
        with open(test_image_path, "rb") as picture:
            django_picture = File(picture)
            portfolio_item = BlogPost(title="Test title",
                                      post="Test post"
                                      )
            portfolio_item.save()
        response = self.client.get("/blog/1/")
        self.assertContains(response, "Test title")
        self.assertContains(response, "Test post")


class PortfolioTestCase(BaseTestCase):

    def test_portfolio(self):
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)


class PortfolioItemTestCase(BaseTestCase):

    def test_portfolio_item_1_404(self):
        response = self.client.get("/portfolio/1/")
        self.assertEqual(response.status_code, 404)

    def test_portfolio_item_1(self):
        test_image_path = BASE_DIR + "/../home/static/images/logo.png"
        with open(test_image_path, "rb") as picture:
            django_picture = File(picture)
            portfolio_item = PortfolioItem(title="Test title",
                                           description="Test desc",
                                           main_image_url=django_picture,
                                           examples1=django_picture,
                                           examples2=django_picture,
                                           examples3=django_picture)
            portfolio_item.save()
        response = self.client.get("/portfolio/1/")
        self.assertContains(response, "Test title")
        self.assertContains(response, "Test desc")


class ContactTestCase(BaseTestCase):

    def test_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)


class SendMailTestCase(BaseTestCase):

    def test_send_mail_post_fail(self):
        response = self.client.post("/send_mail/", follow=True)
        self.assertRedirects(response, "/contact/")
        self.assertContains(response, "Your email failed! Please try again.")

    def test_send_mail_post_success(self):
        self.client.get("/contact/")
        response = self.client.post("/send_mail/",
                                    {"csrfmiddlewaretoken": self.client.cookies["csrftoken"].value,
                                     "message": "Test",
                                     "name": "Ricky Catron",
                                     "sender": "catron.ricky@gmail.com",
                                     "reason": "Job"},
                                    follow=True)
        self.assertRedirects(response, "/contact/")
        self.assertContains(response, "Thanks for your message. I will get back to you shortly.")