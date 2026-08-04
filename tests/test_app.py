import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Log in" in response.data


def test_signup_page_loads(client):
    response = client.get("/signup")
    assert response.status_code == 200
    assert b"Sign Up" in response.data or b"Signup" in response.data


def test_home_requires_login(client):
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]
