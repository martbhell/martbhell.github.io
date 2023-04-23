import requests
from bs4 import BeautifulSoup
import time
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--host", required=True,
                            help="URL to query")
ARGS = parser.parse_args()

base_url = ARGS.host

# Initialize a set to store visited URLs
visited_urls = set()

# Initialize an empty list to store inaccessible links
inaccessible_links = []

# Define a function to fetch and parse a URL
def fetch_url(url):
    # Check if the URL has already been visited
    if url in visited_urls:
        return

    # Add the URL to the visited set
    visited_urls.add(url)

    # Make a request to the URL with a 0.2s timeout
    try:
        response = requests.get(url, timeout=0.2)
    except requests.exceptions.Timeout:
        # If the request times out, add the URL to the inaccessible list and return
        inaccessible_links.append(url)
        return
    except requests.exceptions.RequestException as e:
        # If the request fails for some other reason, print the error message and return
        print("An error occurred while fetching {}: {}".format(url, e))
        return

    # Check if the request was successful
    if response.status_code != 200:
        # If the request failed, add the URL to the inaccessible list and return
        inaccessible_links.append(url)
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links in the page
    links = soup.find_all('a')

    # Loop through all links
    for link in links:
        # Get the link's href attribute
        href = link.get('href')

        # Check if the link is local and accessible
        if href and base_url in href and not href.endswith('#'):
            # Fetch and parse the subpage
            fetch_url(href)
            
            # Sleep for 0.1 seconds to avoid hitting the server too quickly
            time.sleep(0.001)


# Fetch and parse the base URL
fetch_url(base_url)

# If there are any inaccessible links, return non-zero
if inaccessible_links:
    print("The following links are inaccessible:")
    for link in inaccessible_links:
        print(link)
    exit(1)

print("All links are accessible.")

