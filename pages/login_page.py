from core.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    def fill_username(self, username: str) -> None:
        self.page.fill(self.USERNAME_INPUT, username)

    def fill_password(self, password: str) -> None:
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        self.page.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
