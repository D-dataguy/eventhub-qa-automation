def test_config_endpoint_returns_valid_response(api_context):
    response = api_context.get("/api/config")

    assert response.status == 200

    response_data = response.json()

    assert "showExploreLinks" in response_data
    assert isinstance(response_data["showExploreLinks"], bool)
