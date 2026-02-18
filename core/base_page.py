from playwright.sync_api import Page
from core.config import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "") -> None:
        url = f"{settings.base_url}{path}"
        self.page.goto(url)

    def get_title(self):
        return self.page.title()
