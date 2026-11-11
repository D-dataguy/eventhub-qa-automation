from pages.login_page import LoginPage


def test_login_form_elements_visible(page):
    login_page = LoginPage(page)

    login_page.open()

    assert login_page.email_input.is_visible()
    assert login_page.password_input.is_visible()
    assert login_page.sign_in_button.is_visible()
