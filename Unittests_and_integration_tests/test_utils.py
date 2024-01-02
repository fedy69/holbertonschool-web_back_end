#!/usr/bin/env python3
"""Unittest"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 1),
        ({"a": 1}, ("a", "b"), 2),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access nested map exception"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get json"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """A method"""
                return 42

            @memoize
            def a_property(self):
                """A property"""
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, mock_method.return_value)
            self.assertEqual(test.a_property, mock_method.return_value)
            mock_method.assert_called_once()
