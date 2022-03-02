import pytest

from app.endpoints import app

#Alternative to run the file alone
"""
import sys
sys.path.append("../real_app/")
from endpoints import app
"""

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_first_page(client):
    rv = client.get('/')
    assert 'try' in str(rv.data)


def test_health_check(client):
    rv = client.get('/health_check')
    assert 'alive' in str(rv.data)


def test_ts(client):
    rv = client.get('/2021-12-07%2000:00:00')
    assert 'ret' in str(rv.data)
