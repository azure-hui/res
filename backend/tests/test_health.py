def test_health(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    body = response.json()
    assert str(body["code"]) == "0"
    assert body["message"] == "success"
    assert body["data"]["app"]["status"] == "up"
    assert body["data"]["db"]["status"] in ["up", "down"]
    assert "request_id" in body
    assert "timestamp" in body
