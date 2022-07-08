from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from taxi.models import Manufacturer

MANUFACTURER_URL = reverse("taxi:manufacturer-list")

class ManufacturerTestPublic(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_login(self):
        res = self.client.get(MANUFACTURER_URL)

        self.assertNotEqual(res.status_code, 200)

class ManufacturerTestPrivate(TestCase):
    def SetUp(self):
        self.driver = get_user_model().objects.create_user(username="Gor", password=1234)

        self.client.force_login(self.driver)

    def test_retrieve_date(self):
        Manufacturer.objects.create(name="BMW")
        res = self.client.get(MANUFACTURER_URL)
        self.assertEqual(res.status_code, 302)

