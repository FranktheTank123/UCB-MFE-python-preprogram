import pytest
from real_app.endpoints import create_app


@pytest.fixture
def client():
    with create_app().test_client() as client:
        yield client

def test_hello_world(client):
    rv = client.get("/")
    assert "Hello" in str(rv.data)

def test_predict(client):
    rv = client.get("/1/1")
    assert "predict" in str(rv.data)