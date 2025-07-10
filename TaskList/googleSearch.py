from googlesearch import search
import requests
from bs4 import BeautifulSoup

def search_top(query):
    for url in search(query, num_results=5):
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string if soup.title else "No title"
        print(f"{title}\n{url}\n")

if __name__ == "__main__":
    search_top("vimal daga")
