import pytest

import sys
sys.path.append("../real_app/")
from endpoint import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
    # the above 2 line is somewhat equivalent to
    # client = app.test_client()
    # yield client // <-- this means the caller of `client()` can do anything,
    # // but after the caller ends, it will come back to this function
    # client.close()


def test_hello_world(client):
    rv = client.get('/')
    assert 'Hello' in str(rv.data)  # rv.data are bytes

def test_predict_ret_sol(client):
    rv = client.get("/2021-11-01 00:00:00")
    assert "ret_sol" in str(rv.data) 
