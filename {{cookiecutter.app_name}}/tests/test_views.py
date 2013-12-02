# coding: utf-8
from django.test.testcases import TestCase
from {{cookiecutter.app_name}}.models import ...
from factories import ...


class {{cookiecutter.test_case_name}}TestCase(TestCase):
    def test_ping(self):
        response = self.client.get('/?...')
        self.assertEqual(response.status_code, 200)
