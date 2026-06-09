from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    body = response.json()
    assert body["code"] == 0
    assert body["message"] == "healthy"
    assert body["data"]["status"] == "ok"
    assert "request_id" in body
    assert "timestamp" in body