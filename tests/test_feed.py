
def test_public_feed_is_accessible_without_login(client):
    response = client.get("/feed")

    assert response.status_code == 200
    assert b"Public Feed" in response.data


def test_public_feed_displays_existing_posts(authenticated_client):
    authenticated_client.post(
        "/posts/create",
        data={"content": "Hello from the feed"},
    )

    response = authenticated_client.get("/feed")

    assert response.status_code == 200
    assert b"Hello from the feed" in response.data
    assert b"alice" in response.data


def test_public_feed_shows_newest_posts_first(authenticated_client):
    authenticated_client.post(
        "/posts/create",
        data={"content": "First post"},
    )
    authenticated_client.post(
        "/posts/create",
        data={"content": "Second post"},
    )

    response = authenticated_client.get("/feed")

    assert response.status_code == 200
    assert response.data.index(b"Second post") < response.data.index(b"First post")
