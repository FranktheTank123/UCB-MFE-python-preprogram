import pytest
import sys
sys.path.append('/Users/cathy/Desktop/bkl/python/UCB-MFE-python-preprogram/Homeworks/HW9/Ziling_Zhang/')

from real_app.endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    rv = client.get("/")
    assert "Hello" in str(rv.data)


def test_health_check(client):
    rv = client.get("/health_check")
    assert "pong" in str(rv.data)


def test_predict_rel_sol(client):
    rv = client.get("/2021-11-01 00:00:00")
    assert "ret_sol" in str(rv.data)