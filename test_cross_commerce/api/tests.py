from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory


class APITests(SimpleTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()


    def test_api_status_code(self):
        """
        Test if API is ok
        """
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_api_is_sorted(self):
        """
        Test if API data is sorted
        """
        response = self.client.get('/api/')
        self.assertTrue(self.is_sorted(response.data))


    def is_sorted(self, arr):
        """
        Check if each comparison returns 1 (True)
        If any comparison is 0 (False), it should not pass.
        """
        if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
            return True
        return False
