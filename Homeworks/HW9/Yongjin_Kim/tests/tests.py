import pytest
import sys
import os

root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
from Yongjin_Kim.real_app.endpoints import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_HW9(client):
    rv = client.get('/')
    assert 'HW9' in str(rv.data)  # rv.data are bytes

def test_HW8(client):
    rv = client.get('/')
    assert 'HW8' in str(rv.data)  # rv.data are bytes