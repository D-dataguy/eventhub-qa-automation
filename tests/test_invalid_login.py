import json
from pathlib import Path

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


DATA_PATH = Path(__file__).parent.parent / "test_data" / "login_data.json"

with open(DATA_PATH, encoding="utf-8") as file:
    LOGIN_CASES = json.load(file)


@pytest.mark.parametrize("test_data", LOGIN_CASES, ids=lambda data: data["test_case"])
def test_invalid_login(page, test_data):

    login_page = LoginPage(page)
    login_page.open()

    login_page.enter_credentials(test_data["email"], test_data["password"])

    with page.expect_response(
        lambda response: (
            "/api/auth/login" in response.url and response.request.method == "POST"
        )
    ) as response_info:
        login_page.submit_login()
    assert response_info.value.status == 400

    print("LOGIN API RESPONSE:", response_info.value.text())
    expect(login_page.error_message).to_be_visible()

    expect(page).to_have_url(login_page.URL)
