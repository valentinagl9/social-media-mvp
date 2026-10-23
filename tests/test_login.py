import sqlite3

import pytest
from werkzeug.security import generate_password_hash

from app import create_app


@pytest.fixture()
def app(tmp_path):
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "test-secret",
            "DATABASE": str(tmp_path / "test.sqlite"),
        }
    )
    with sqlite3.connect(app.config["DATABASE"]) as db:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("alice", generate_password_hash("strong-pass-123")),
        )
        db.commit()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Log in" in response.data


def test_valid_credentials_start_session(client):
    response = client.post(
        "/login",
        data={"username": "alice", "password": "strong-pass-123"},
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/home")

    response = client.get("/home")
    assert response.status_code == 200
    assert b"Welcome, alice!" in response.data


def test_invalid_password_is_rejected(client):
    response = client.post(
        "/login",
        data={"username": "alice", "password": "wrong-password"},
    )
    assert response.status_code == 401
    assert b"Invalid username or password" in response.data


def test_unknown_username_is_rejected(client):
    response = client.post(
        "/login",
        data={"username": "unknown", "password": "strong-pass-123"},
    )
    assert response.status_code == 401
    assert b"Invalid username or password" in response.data


def test_home_requires_login(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")
