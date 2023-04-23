
import requests
from bs4 import BeautifulSoup

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--host", required=True,
                            help="URL to query")
ARGS = parser.parse_args()

url = ARGS.host

response = requests.get(url)
if response.status_code != 200:
    print("Error: Status code", response.status_code)
    exit(1)

soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")

for link in links:
    href = link.get("href")
    if href and href.startswith("http") and url in href:
        response = requests.get(href)
        if response.status_code != 200:
            print("Error: Broken link", href)
            exit(1)
        if response.status_code == 200:
            print("OK LINK", href)
