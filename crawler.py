import requests
from bs4 import BeautifulSoup
import urllib.parse

def crawl_site(base_url, max_pages=5):
    """Explore le site pour récupérer des URLs exploitables plus rapidement."""
    visited = set()
    to_visit = [base_url]
    found_urls = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=3)
            visited.add(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                for link in soup.find_all("a", href=True):
                    new_url = urllib.parse.urljoin(base_url, link["href"])

                    if new_url.startswith(base_url) and new_url not in visited:
                        to_visit.append(new_url)
                        found_urls.append(new_url)

        except requests.RequestException:
            continue

    return found_urls[:max_pages]  # 🔥 Retourne seulement `max_pages` URLs
