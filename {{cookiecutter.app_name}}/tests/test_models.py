# coding: utf-8
from decimal import Decimal
from django.test.testcases import TestCase
from factories import ..


class {{cookiecutter.test_case_name}}TestCase(TestCase):
    def test_model_unicode(self):
        ...
        self.assertEqual(unicode(...), ...)
