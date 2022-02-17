import pytest
import sys
sys.path.append("../real_app/")
from endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_welcome_page(client):
    rv = client.get('/')
    assert 'Welcome' in str(rv.data)  # rv.data are bytes


def test_predict(client):
    rv = client.get('/2021-11-01 00:00:00')
    assert 'ret_sol' in str(rv.data)
