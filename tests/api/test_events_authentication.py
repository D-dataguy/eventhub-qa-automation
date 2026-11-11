def test_events_endpoint_without_token(api_context):
    response = api_context.get("/api/events?limit=6")

    print("STATUS CODE:", response.status)

    assert response.status in [401, 403]


def test_events_endpoint_with_invalid_token(api_context):
    response = api_context.get(
        "/api/events?limit=6",
        headers={"Authorization": "Bearer invalid_token_123"},
    )

    print("STATUS CODE:", response.status)

    assert response.status in [401, 403]
