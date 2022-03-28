from django.test import TestCase

from juliany_pizza.home.forms import ProfileDetailsForm, ContactForm


class TestProfileDetailsForm(TestCase):
    def test_profile_deatails_form_valid(self):
        data = {
            'first_name': 'Test',
            'last_name': 'Testov',
            'phone': '0899999999',
            'address': 'address 1'
        }
        form = ProfileDetailsForm(data)
        self.assertTrue(form.is_valid())


class TestContactForm(TestCase):
    def test_send_mail(self):
        data = {
            'name': 'sender',
            'message': 'message here',
            'subject': 'Subject here'
        }
        form = ContactForm(data)
        self.assertTrue(form.is_valid())
        form.send_mail()
