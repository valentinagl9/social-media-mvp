
def test_authenticated_user_can_create_post(authenticated_client, app):
    response = authenticated_client.post(
        "/posts/create",
        data={"content": "My first post"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"My first post" in response.data

    with app.app_context():
        from app.db import get_db

        post = get_db().execute(
            "SELECT content FROM posts WHERE content = ?",
            ("My first post",),
        ).fetchone()

    assert post is not None


def test_post_with_empty_content_is_rejected(authenticated_client, app):
    response = authenticated_client.post(
        "/posts/create",
        data={"content": "   "},
        follow_redirects=True,
    )

    assert response.status_code == 200

    with app.app_context():
        from app.db import get_db

        posts = get_db().execute("SELECT * FROM posts").fetchall()

    assert len(posts) == 0


def test_unauthenticated_user_cannot_create_post(client, app):
    response = client.post(
        "/posts/create",
        data={"content": "This should not be saved"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")

    with app.app_context():
        from app.db import get_db

        posts = get_db().execute("SELECT * FROM posts").fetchall()

    assert len(posts) == 0
