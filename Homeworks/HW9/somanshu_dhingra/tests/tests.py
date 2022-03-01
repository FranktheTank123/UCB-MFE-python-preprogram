import pytest
import sys

sys.path.append("../real_app/")
from endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_welcome(client):
    rv = client.get('/')
    assert 'WELCOME' in str(rv.data)


def test_health(client):
    rv = client.get('/health_check')
    assert 'OK' in str(rv.data)

def test_predict(client):
    rv = client.get('/predict')
    assert 'predict' in str(rv.data)