import random
from unittest import TestCase

from .quick_sort import quick_sort
from .is_sorted_check import is_sorted


class TestQuickSort(TestCase):
    def setUp(self):
        self.random_numbers = random.sample(range(-1000, 1000), 97)
        self.sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 97, 124, 1087, 3989]
        self.inversed = [1017, 81, 70, 65, 64, 63, 42, 5, 4, 3, 2, 1]
        self.repeated = [97, 42, 10, 111, 111, 111, 97, 42, 10, 10, 97, 42]

    def test_sort_random_numbers(self):
        """
        Test Quick Sort in Random Numbers List
        """
        arr = self.random_numbers
        quick_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_sort_already_sorted_numbers(self):
        """
        Test Quick Sort in Already Sorted Numbers List
        """
        arr = self.sorted
        quick_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_sort_inversed_numbers(self):
        """
        Test Quick Sort in Inversed Numbers List
        """
        arr = self.inversed
        quick_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_sort_repeated_numbers(self):
        """
        Test Quick Sort in Repeated Numbers List
        """
        arr = self.repeated
        quick_sort(arr)
        self.assertTrue(is_sorted(arr))
