import pytest

from real_app.endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello(client):
    rv = client.get("/")
    assert "Hello!" in str(rv.data)


def test_predict(client):
    rv = client.get("/predict-0")
    assert ("Cercevelik" in str(rv.data)) or ("UrgupSivrisi" in str(rv.data))
