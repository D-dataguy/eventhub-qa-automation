import json
from pathlib import Path

import pytest

from config.settings import API_BASE_URL


DATA_PATH = Path(__file__).parent.parent.parent / "test_data" / "login_data.json"

with open(DATA_PATH, encoding="utf-8") as file:
    LOGIN_CASES = json.load(file)


@pytest.mark.parametrize("test_data", LOGIN_CASES, ids=lambda data: data["test_case"])
def test_invalid_login_api(api_context, test_data):

    response = api_context.post(
        "/api/auth/login",
        data={"email": test_data["email"], "password": test_data["password"]},
    )

    assert response.status == 400

    response_data = response.json()

    assert response_data["success"] is False
    assert response_data["error"] == "Invalid email or password"
    assert response_data["details"] == []
