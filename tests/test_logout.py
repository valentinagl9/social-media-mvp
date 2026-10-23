def test_logout_clears_session(authenticated_client):
    response = authenticated_client.post("/logout")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")

    with authenticated_client.session_transaction() as session:
        assert "user_id" not in session
        assert "username" not in session


def test_home_is_inaccessible_after_logout(authenticated_client):
    authenticated_client.post("/logout")
    response = authenticated_client.get("/home")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")
