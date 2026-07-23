from tools.browser import BrowserTool

browser = BrowserTool()

browser.start()

browser.open("https://example.com")

print("Title :", browser.title())

print("Heading :", browser.text("h1"))

browser.screenshot("example.png")

browser.close()