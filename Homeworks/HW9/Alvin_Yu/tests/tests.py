import pytest
from endpoints import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_model_Generator(client):
    rv = client.get('/')
    assert "I will predict price of Solano at a given time. Go to /Help for details." in str(rv.data)

def test_HelpMessage(client):
    rv = client.get("/Help")
    assert isinstance(rv,(str))

def test_predict_rel_sol(client):
    rv = client.get("/2021-11-01_00:00:00")
    asset isinstance(rv,(dict))
