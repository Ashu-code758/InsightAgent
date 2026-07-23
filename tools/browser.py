from playwright.sync_api import sync_playwright


class BrowserTool:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

    def open(self, url):
        self.page.goto(url)

    def title(self):
        return self.page.title()

    def click(self, selector):
        self.page.click(selector)

    def type(self, selector, text):
        self.page.fill(selector, text)

    def wait(self, seconds):
        self.page.wait_for_timeout(seconds * 1000)

    def html(self):
        return self.page.content()

    def screenshot(self, filename):
        self.page.screenshot(path=filename)

    def text(self, selector):
        return self.page.locator(selector).inner_text()

    def close(self):
        self.browser.close()
        self.playwright.stop()