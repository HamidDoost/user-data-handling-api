from app.api import health


def test_health(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!", "environment": "dev", "testig": True}
