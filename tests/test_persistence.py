
import sqlite3

from werkzeug.security import generate_password_hash


def test_user_data_persists_after_database_reconnect(app):
    database_path = app.config["DATABASE"]

    with sqlite3.connect(database_path) as db:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("persistent_user", generate_password_hash("strong-pass-123")),
        )
        db.commit()

    with sqlite3.connect(database_path) as db:
        user = db.execute(
            "SELECT username FROM users WHERE username = ?",
            ("persistent_user",),
        ).fetchone()

    assert user is not None
    assert user[0] == "persistent_user"


def test_post_data_persists_after_database_reconnect(app):
    database_path = app.config["DATABASE"]

    with sqlite3.connect(database_path) as db:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("post_author", generate_password_hash("strong-pass-123")),
        )
        db.commit()

        db.execute(
            "INSERT INTO posts (user_id, content) VALUES (?, ?)",
            (1, "A persistent post"),
        )
        db.commit()

    with sqlite3.connect(database_path) as db:
        post = db.execute(
            "SELECT content FROM posts WHERE content = ?",
            ("A persistent post",),
        ).fetchone()

    assert post is not None
    assert post[0] == "A persistent post"
