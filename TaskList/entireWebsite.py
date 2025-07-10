import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Target URL
base_url = "https://Netflix.com"
folder = "downloaded_site"
os.makedirs(folder, exist_ok=True)

# Headers for spoofing a browser request
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch homepage
response = requests.get(base_url, headers=headers, stream=True)
response.raw.decode_content = False
html_content = response.raw.read().decode('utf-8', errors='ignore')
soup = BeautifulSoup(html_content, 'html.parser')


# Save HTML
with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Function to download any file
def download_file(file_url):
    try:
        parsed = urlparse(file_url)
        if not parsed.scheme:  # Skip invalid links
            return
        filename = os.path.basename(parsed.path)
        if not filename:
            return
        full_path = os.path.join(folder, filename)
        if not os.path.exists(full_path):
            r = requests.get(file_url, headers=headers)
            with open(full_path, "wb") as f:
                f.write(r.content)
            print(f"Downloaded: {file_url}")
    except Exception as e:
        print(f"Error downloading {file_url} → {e}")

# Collect resource links
resources = set()

# 1. Images
for tag in soup.find_all("img", src=True):
    resources.add(urljoin(base_url, tag["src"]))

# 2. CSS files
for tag in soup.find_all("link", rel="stylesheet"):
    resources.add(urljoin(base_url, tag["href"]))

# 3. JS files
for tag in soup.find_all("script", src=True):
    resources.add(urljoin(base_url, tag["src"]))

# 4. PDFs or other downloads
for tag in soup.find_all("a", href=True):
    href = tag["href"]
    if any(href.endswith(ext) for ext in [".pdf", ".docx", ".zip", ".pptx", ".xlsx"]):
        resources.add(urljoin(base_url, href))

# Download all collected resources
for file_url in resources:
    download_file(file_url)
