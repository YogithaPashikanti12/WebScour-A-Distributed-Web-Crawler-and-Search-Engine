import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

# 1
def crawl(seed_url):
    # 2
    queue = []
    visited = set()

    queue.append(seed_url)
    # 3. folder creation
    os.makedirs("pages", exist_ok=True)
    page_count = 0
    #4. Crawling loop
    while queue and page_count < 5:
        url = queue.pop(0)

        if url in visited:
            continue

        try:
            # 5 Fetching Webpages
            print(f"Fetching: {url}")
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                continue
            # 6. Handling relative links
            html = response.text
            base_tag = f'<base href="{url}">\n'
            html = base_tag + html

        except requests.exceptions.RequestException:
            continue

        page_count += 1
        # Saving the webpages
        filename = f"pages/page_{page_count}.html"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(html)

        print(f"Saved: page_{page_count}.html")
        # Extracting Links
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")

        for tag in links:
            href = tag.get("href")
            if href:
                absolute_link = urljoin(url, href)
                # Discovering New pages
                if absolute_link not in visited and absolute_link not in queue:
                    queue.append(absolute_link)

        visited.add(url)
        print(f"Extracted {len(links)} links\n")
        time.sleep(1)

    print("Crawling Finished")
    print("Total pages crawled:", page_count)
    print("Total unique URLs visited:", len(visited))


crawl("https://www.python.org")
