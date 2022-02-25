import pytest

from real_app.endpoint import app

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client
        
def test_check(client):
    rv = client.get('/test/avocado')
    assert 'vocad' in str(rv.data)  # rv.data are bytes

def test_predict(client):
    rv = client.get("/2019-08-08")
    assert "ret" in str(rv.data) and "4" in str(rv.data)