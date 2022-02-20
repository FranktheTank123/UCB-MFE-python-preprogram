import pytest
import sys
sys.path.append("../real_app/")
from endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_front_page(client):
    rv = client.get('/')
    assert 'Welcome' in str(rv.data)  # rv.data are bytes