from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory

from test_cross_commerce.utils.is_sorted_check import is_sorted


class APITests(SimpleTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_api_status_code(self):
        """
        Test if API is ok
        """
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)

    def test_api_is_sorted(self):
        """
        Test if API data is sorted
        """
        response = self.client.get("/api/")
        self.assertTrue(is_sorted(response.data))
