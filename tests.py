"""
Module contains unit testing code for the fetch_url_with_html_tree function in the functions.py module.
Source: https://stackoverflow.com/questions/15753390/how-can-i-mock-requests-and-the-response
"""

import io
import unittest
from unittest.mock import Mock, patch
from requests.exceptions import HTTPError
import requests
from functions import fetch_url_with_html_tree


class TestFetchUrlWithHtmlTree(unittest.TestCase):
    @patch('os.path.exists')
    @patch('builtins.open')
    @patch('requests.get')
    def test_url_in_file(self, mock_get, mock_open, mock_exists):
        """
        Test case for when the URL is already in the file.
        The function should return the corresponding data from the file.        
        """
        mock_exists.return_value = True
        mock_open.return_value.__enter__.return_value = io.StringIO('{"https://www.example.com": "data"}')
        result = fetch_url_with_html_tree('https://www.example.com')
        self.assertEqual("data", result)

    @patch('os.path.exists')
    @patch('requests.get')
    def test_url_not_in_file_success(self, mock_get, mock_exists):
        """
        Test case for when the URL is not in the file but successfully fetch the title and abstract data.
        
        """
        mock_exists.return_value = False

        mock_response = Mock()
        mock_response.text = '<html><h1><span>title:</span>title</h1><blockquote><span>abstract:</span>abstract</blockquote></html>'

        mock_get.return_value = mock_response

        result = fetch_url_with_html_tree('https://www.someurl.com')
        self.assertEqual({"title": ["title"], "abstract": ["abstract"]}, result)

    @patch('os.path.exists')
    @patch('requests.get')
    def test_url_not_in_file_fail(self, mock_get, mock_exists):
        mock_exists.return_value = False
        mock_get.side_effect = requests.RequestException
        result = fetch_url_with_html_tree('https://www.example.com')
        self.assertEqual(None, result)

    @patch('os.path.exists')
    @patch('requests.get')
    def test_url_not_in_file_empty(self, mock_get, mock_exists):
        mock_exists.return_value = False
        mock_get.return_value.text = ''
        result = fetch_url_with_html_tree('https://www.example.com')
        self.assertEqual(None, result)
  
  
if __name__ == '__main__':
    unittest.main()
