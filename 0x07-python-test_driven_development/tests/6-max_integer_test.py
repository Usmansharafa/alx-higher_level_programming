#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_ordered_list(self):
        """Tests an ordered list"""
        self.assertEqual(max_integer([1, 3, 7, 200]), 200)

    def test_unordered_list(self):
        """Tests an unordered list"""
        self.assertEqual(max_integer([1, 2, 7, 4]), 7)

    def test_max_at_the_beginning(self):
        """Tests a list with max num at the beginning"""
        self.assertEqual(max_integer([2000, -120, 300, 500]), 2000)

    def test_one_element_list(self):
        """Tests a one element list"""
        self.assertEqual(max_integer([20]), 20)

    def test_list_of_floats(self):
        """Tests a list of floats"""
        self.assertEqual(max_integer([1.23, 2.23, 3.50, 20.21, 10.5]), 20.21)

    def test_list_of_ints_and_floats(self):
        """"Tests a list of ints and floats"""
        self.assertEqual(max_integer([1, 2.40, 30.25, 100]), 100)

    def test_string(self):
        """Tests a string"""
        self.assertEqual(max_integer("boy"), "y")

    def test_list_of_strings(self):
        """Tests a lists of strings"""
        self.assertEqual(max_integer(["boy", "girl", "man", "cat"]), "man")

    def test_empty_string(self):
        """"Tests an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_exceptions(self):
        """Tests with parameters that raises exceptions"""
        with self.assertRaises(TypeError):
            max_integer(5)
            max_integer(["hello", 1, 2, 3, 5])

        with self.assertRaises(KeyError):
            max_integer({"1": 1, "2": 2})


if __name__ == "__main__":
    unittest.main()
