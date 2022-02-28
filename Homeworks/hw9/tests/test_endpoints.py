import pytest
import sys
sys.path.append("../real_app/")
from endpoints import app



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get("/")
    assert 'Hello' in str(rv.data)

def test_predict(client):
    rv = client.get('/2021-11-02 00:00:00')
    assert 'ret_sol' in str(rv.data)


def test_all(client):
    rv = client.get('all/ADA/2021-11-02 00:00:00')
    assert 'RET_' in str(rv.data)


def test_VOL(client):
    rv = client.get('ADA/2021-12-01 20:00:00')
    assert 'VOl_' in str(rv.data)