import pytest
from real_app.endpoints import app


@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_ping(client):
	rv = client.get('/ping')
	assert 'pong' in str(rv.data)


# def test_predict(client):
# 	rv = client.get('/get_prediction/J7Xvjkte')
# 	# assert 'predicted value'  in str(rv.data)
