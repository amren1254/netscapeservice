import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from lxml.etree import Element, SubElement, tostring
from datetime import datetime


def normalize_url(url):
    """
    Normalize a URL by removing query parameters and fragments.
    """
    parsed = urlparse(url)
    return parsed.scheme + "://" + parsed.netloc + parsed.path


def generate_sitemap(urls):
    """
    Generates an XML sitemap from a list of URLs, including lastmod and priority.
    """
    urlset = Element(
        "urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in urls:
        url_element = SubElement(urlset, "url")
        loc = SubElement(url_element, "loc")
        loc.text = url
        lastmod = SubElement(url_element, "lastmod")
        # Use current time; adjust as needed
        lastmod.text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        priority = SubElement(url_element, "priority")
        # Adjust logic as needed
        priority.text = "1.00" if url == "http://netscapeservice.com/" else "0.80"
    return tostring(urlset, pretty_print=True, xml_declaration=True, encoding="UTF-8")


def get_all_site_links(url):
    urls_visited = set()
    urls_to_visit = set([url])

    while urls_to_visit:
        current_url = urls_to_visit.pop()
        if current_url in urls_visited:
            continue

        print(f"Crawling: {current_url}")
        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_visited.add(current_url)

            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(current_url, href)
                full_url = normalize_url(full_url)

                if urlparse(full_url).scheme and urlparse(full_url).netloc:
                    if urlparse(full_url).netloc == urlparse(url).netloc:
                        urls_to_visit.add(full_url)

        except requests.RequestException as e:
            print(f"Failed to fetch {current_url}: {e}")

    return urls_visited


if __name__ == "__main__":
    website_url = "http://netscapeservice.com/"  # Change to your target website URL
    urls = get_all_site_links(website_url)
    print(f"Found {len(urls)} URLs.")
    sitemap = generate_sitemap(urls)
    with open("sitemap.xml", "wb") as file:
        file.write(sitemap)
    print("Sitemap generated and saved to sitemap.xml.")
