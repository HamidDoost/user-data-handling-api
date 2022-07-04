def test_get_users(test_app):

    response = test_app.get("/users/")
    assert response.status_code == 200
    # Todo: fix this when correct mocking with FastAPI
    # assert response.json() == []


def test_add_user(test_app):
    data = {
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "phone": "string",
        "age": 0,
    }

    response = test_app.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json() == {**data, "id": response.json()["id"]}
