#!/usr/bin/env python3

import urllib.request


def fetch_url(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content


def print_response_info(content):
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content}")


def main():
    url = 'https://alx-intranet.hbtn.io/status'
    content = fetch_url(url)
    print_response_info(content)


if __name__ == '__main__':
    main()

