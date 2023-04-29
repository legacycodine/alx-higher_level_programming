#!/usr/bin/python3
"""
Fetches the status of https://intranet.hbtn.io/status.
"""

import urllib.request

# URL to fetch
url = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':
    # Send a request to the URL and read the response
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        # Print the response information
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf8_content}")

