from bs4 import BeautifulSoup

class ScraperTool:

    def parse(self, html):
        if not html:
            return None
        return BeautifulSoup(html, "html.parser")

    def title(self, soup):
        if soup and soup.title and soup.title.string:
            return soup.title.string.strip()
        return "No Title Found"

    def heading(self, soup):
        if not soup:
            return None
        h1 = soup.find("h1")
        return h1.get_text(strip=True) if h1 else None

    def links(self, soup):
        if not soup:
            return []
        # Sirf valid href links collect karega
        return [
            link.get("href") 
            for link in soup.find_all("a") 
            if link.get("href")
        ]