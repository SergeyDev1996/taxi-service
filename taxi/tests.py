from django.test import TestCase
from taxi.models import Manufacturer, Driver, Car


class ModelsTests(TestCase):
    def test_manufacturer_credentials(self):
        manufacturer = Manufacturer.objects.create(name="LAZ", country="Ukraine")
        full_manufacturer = manufacturer.name + ' ' + manufacturer.country
        self.assertEqual(str(manufacturer), full_manufacturer)

    def test_driver_data(self):
        driver = Driver.objects.create(username="Dimon91", first_name="Dima", last_name="Bogun")
        self.assertEqual(str(driver), "Dimon91 (Dima Bogun)")

    def test_car_model(self):
        manufacturer = Manufacturer.objects.create(name="Zaz", country="Ukraine", id=1)
        car = Car.objects.create(model="BMWx25", manufacturer_id=1)
        self.assertEqual(str(car), "BMWx25")