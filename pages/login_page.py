from config.settings import BASE_URL


class LoginPage:
    URL = f"{BASE_URL}/login"

    def __init__(self, page):
        self.page = page

        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.sign_in_button = page.locator("button[type='submit']")
        self.error_message = page.get_by_text("Invalid email or password", exact=True)

    def open(self):
        self.page.goto(self.URL)

    def enter_credentials(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def submit_login(self):
        self.sign_in_button.click()
