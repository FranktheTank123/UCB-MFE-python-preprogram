import io
import os
import sys

import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
print(parent)

from endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_main(client):

    rv = client.get("/")
    assert rv.status_code == 200


