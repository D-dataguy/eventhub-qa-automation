from config.settings import EVENTHUB_EMAIL, EVENTHUB_PASSWORD


def test_successful_login_api(api_context):

    response = api_context.post(
        "/api/auth/login", data={"email": EVENTHUB_EMAIL, "password": EVENTHUB_PASSWORD}
    )

    response_data = response.json()

    assert response.status == 200
    assert isinstance(response_data["user"]["id"], int)
    assert response_data["user"]["email"] == EVENTHUB_EMAIL
