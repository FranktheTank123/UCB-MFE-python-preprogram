import struct

import pytest

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


def test_shape(client):
    rv = client.get("/shape")
    assert "shape" in str(rv.data)


def test_ret_sol(client):
    rv = client.get("/ret_SOL")
    assert "min" in str(rv.data)


def test_count_null(client):
    rv = client.get("/count_null")
    assert "null" in str(rv.data)


def test_correlation(client):
    rv = client.get("/correlation")
    assert "ret" in str(rv.data)


def test_rmse(client):
    rv = client.get("/RMSE")
    assert "RMSE" in str(rv.data)
