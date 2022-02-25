import sys
import os
sys.path.append(os.getcwd()+'/real_app')

import pytest
from endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_welcome(client):
    rv = client.get('/')
    assert "Xiaowen Cao's app" in str(rv.data)  # rv.data are bytes


def test_check(client):
    rv = client.get('/health_check')
    assert 'good' in str(rv.data)  



def test_predict_rel_sol(client):
    rv = client.get('/2021-11-01 00:00:00')
    
    assert "ret_sol" in str(rv.data)
