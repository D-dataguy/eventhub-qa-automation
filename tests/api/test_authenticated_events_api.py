from config.settings import EVENTHUB_EMAIL, EVENTHUB_PASSWORD


def test_authenticated_user_can_get_events(api_context):

    # Step 1: Authenticate
    login_response = api_context.post(
        "/api/auth/login", data={"email": EVENTHUB_EMAIL, "password": EVENTHUB_PASSWORD}
    )

    assert login_response.status == 200

    login_data = login_response.json()
    token = login_data["token"]

    # Step 2: Send authenticated request
    events_response = api_context.get(
        "/api/events?limit=6", headers={"Authorization": f"Bearer {token}"}
    )

    # Step 3: Validate response
    assert events_response.status == 200

    events_data = events_response.json()

    assert events_data["success"] is True
    assert isinstance(events_data["data"], list)
    assert isinstance(events_data["pagination"], dict)

    assert events_data["pagination"]["limit"] == 6

    print("Authenticated events request passed.")
    print("Events returned:", len(events_data["data"]))
