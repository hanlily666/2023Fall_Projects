"""

"""
import requests
from requests.exceptions import RequestException
import lxml.html
import lxml.etree as etree
import json
import os
from time import sleep


def fetch_url_with_html_tree(url: str, max_attempts: int = 3) -> lxml.etree:
    """
    Fetches the HTML of a webpage and parses it into an lxml HTML tree.

    :param url: The URL of the webpage.
    :param max_attempts: The maximum number of attempts to fetch the webpage.
    :return: An lxml HTML tree, or None if an error occurred.

    >>> fetch_url_with_html_tree('https://www.forbes.com/sites/cindygordon/2022/?sh=5c2410226989')
    
    """
    # Check if the URL is already in the JSON file
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
            # request_count += 1
            r = requests.get(url)
            request_count += 1
            if r.text.strip() == "":
                print(f"Empty response from {url}. Skipping this URL.")
                return None
            # tree = lxml.html.fromstring(r.text)
            # Save the URL and the HTML content to the JSON file
            # with open('urls.json', 'a') as f:
            #     json.dump({url: r.text}, f)
            #     f.write('\n')
        except RequestException as e:
            if request_count == max_attempts:
                print("Repeated requests still don't work. Giving up.")
                return None
            else:
                t = 10 * request_count  # number of seconds to wait.
                print('Error retrieving web page. Will retrying in {t} seconds...')
                sleep(t)
    return tree
