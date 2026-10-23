import sqlite3

import pytest
from werkzeug.security import check_password_hash

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
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_registration_page_loads(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Create an account" in response.data


def test_user_can_register_with_hashed_password(app, client):
    response = client.post(
        "/register",
        data={"username": "alice", "password": "strong-pass-123"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Account created successfully" in response.data

    with sqlite3.connect(app.config["DATABASE"]) as db:
        user = db.execute(
            "SELECT username, password_hash FROM users WHERE username = ?",
            ("alice",),
        ).fetchone()

    assert user is not None
    assert user[0] == "alice"
    assert user[1] != "strong-pass-123"
    assert check_password_hash(user[1], "strong-pass-123")


def test_duplicate_username_is_rejected(client):
    data = {"username": "alice", "password": "strong-pass-123"}
    assert client.post("/register", data=data).status_code == 302

    response = client.post("/register", data=data)
    assert response.status_code == 409
    assert b"already taken" in response.data


@pytest.mark.parametrize(
    "data",
    [
        {"username": "", "password": "strong-pass-123"},
        {"username": "alice", "password": ""},
        {"username": "alice", "password": "short"},
    ],
)
def test_invalid_registration_is_rejected(client, data):
    response = client.post("/register", data=data)
    assert response.status_code == 400
