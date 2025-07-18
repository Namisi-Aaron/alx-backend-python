#!/usr/bin/env python
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

import unittest

class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test for the `access_nested_map` function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """
        Tests the access_nested_map function with different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_value)