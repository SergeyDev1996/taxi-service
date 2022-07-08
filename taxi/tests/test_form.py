from django.test import TestCase

from taxi.form import DriverForm

class FormTests(TestCase):
    def test_license_number_incorrect(self):
        form_data = {
            "username" : "andrey",
            "first_name": "Test First",
            "last_name": "Test last",
            "license_number": "ABC12345"
        }
        form = DriverForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)