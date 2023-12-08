"""
This module contains functions that are imported into the Jupyter Notebook. 
These functions facilitate the data analysis process, providing a clearer understanding for the reader.
"""
import re
import requests
from requests.exceptions import RequestException
import lxml.html
import lxml.etree as etree
import json
import os
from urllib.parse import urlparse


def extract_the_hostname(url: str) -> str:
    """
    Extract the hostname from the url.

    :param url: The URL of the webpage.
    :return: hostname of the url.
    >>> extract_the_hostname('https://stackoverflow.com/questions/39901550/python-userwarning-this-pattern-has-match-groups-to-actually-get-the-groups')
    'stackoverflow.com'

    >>> extract_the_hostname('ddd') is None
    True
    """
    hostname = urlparse(url).hostname
    return hostname if hostname else None


def fetch_url_with_html_tree(url: str, max_attempts: int = 3) -> lxml.etree:
    """
    Fetches the HTML of a webpage and parses it into a lxml HTML tree. If the URL has been 
    parsed, return the information of that URL from the usls.json.
    The test for this function is in tests.py module.

    :param url: The URL of the webpage.
    :param max_attempts: The maximum number of attempts to fetch the webpage.
    :return: A lxml HTML tree, or None if an error occurred.
    """
    if os.path.exists('urls.json'):
        with open('urls.json', 'r') as f:
            for line in f:
                data = json.loads(line)
                if url in data:
                    # If the URL is in the file, return the saved HTML content
                    return data[url]

    # If the URL is not in the file, fetch the webpage
    tree = None
    request_count = 0
    while tree is None:
        try:
            request_count += 1
            r = requests.get(url)
            if r.text.strip() == "":
                print(f"Empty response from {url}. Skipping this URL.")
                return None
            content = r.text
            # Remove XML and Unicode declarations
            content = re.sub(r'^\s*<\?xml.*\?>', '', content)
            content = re.sub(r'^\s*<\?unicode.*\?>', '', content)
            tree = lxml.html.fromstring(content)        
            title = tree.xpath('//h1/span/following-sibling::text()')
            abstract = tree.xpath('//blockquote/span/following-sibling::text()')
            with open('urls.json', 'a') as f:
                json.dump({url: {"title": title, "abstract": abstract}}, f)
                f.write('\n')
        except RequestException as e:
            print(f"Error retrieving {url}. Attempt {request_count}.")
            if request_count == max_attempts:
                print(f"Failed to retrieve {url} after {max_attempts} attempts. Skipping this URL.")
                with open('urls.json', 'a') as f:
                    json.dump({url: str(e)}, f)
                    f.write('\n')
                return None
    return {"title": title, "abstract": abstract}


if __name__ == '__main__':
    pass
