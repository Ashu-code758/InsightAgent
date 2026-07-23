from tools.browser import BrowserTool
from tools.scraper import ScraperTool

browser = BrowserTool()
scraper = ScraperTool()

browser.start()

browser.open("https://example.com")

html = browser.html()

soup = scraper.parse(html)

print(scraper.title(soup))
print(scraper.heading(soup))
print(scraper.links(soup))

browser.close()