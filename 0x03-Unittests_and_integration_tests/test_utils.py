#!/usr/bin/env python3
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json

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
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests the access_nested_map function with a KeyError
        and checks that the exception message is correct
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), repr(path[-1]))

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, url, payload, mock_get):
        """
        Tests the get_json function with different inputs.
        """
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        result = get_json(url)
            
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)
        


