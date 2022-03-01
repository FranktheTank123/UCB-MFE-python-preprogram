import pytest

from real_app.endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
    # the above 2 line is somewhat equivalent to
    # client = app.test_client()
    # yield client // <-- this means the caller of `client()` can do anything,
    # // but after the caller ends, it will come back to this function
    # client.close()


def test_home(client):
    rv = client.get('/')
    assert 'SOL' in str(rv.data)  # rv.data are bytes


#def test_login(client):
#    rv = client.get('/login')
#   assert 'GET' in str(rv.data)

#    rv = client.post('/login')
#    assert 'POST' in str(rv.data)
