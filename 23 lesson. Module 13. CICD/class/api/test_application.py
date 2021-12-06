import pytest

from application.app import app, db
from application.database import User


@pytest.fixture
def client():
    # init_DB()
    yield app.test_client()
    truncate_DB()


def truncate_DB():
    with app.app_context():
        User.query.delete()
        db.session.commit()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_response(client):
    response = client.get("/")
    assert b"Hello" in response.data


def test_add(client):
    with app.app_context():
        test_data = {"name": "Peter", "count": 33}
        client.post("/user", json=test_data)
        assert User.query.count() == 1


if __name__ == "__main__":
    pytest.main()
