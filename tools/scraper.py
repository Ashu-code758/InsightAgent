from bs4 import BeautifulSoup


class ScraperTool:

    def parse(self, html):
        return BeautifulSoup(html, "html.parser")

    def title(self, soup):
        return soup.title.text

    def heading(self, soup):
        h1 = soup.find("h1")
        return h1.text if h1 else None

    def links(self, soup):
        return [link.get("href") for link in soup.find_all("a")]