class BasePage:
    def __init__(self, page, timeout=5000):
        self.page=page
        self.timeout=timeout

    def open_page(self, link):
        self.page.goto(link)