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
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def authenticated_client(app):
    with sqlite3.connect(app.config["DATABASE"]) as db:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("alice", generate_password_hash("strong-pass-123")),
        )
        db.commit()

    client = app.test_client()
    with client.session_transaction() as session:
        session["user_id"] = 1
        session["username"] = "alice"

    return client
