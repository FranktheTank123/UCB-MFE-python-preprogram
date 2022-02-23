import pytest

import sys
sys.path.append("../real_app/")
from endpoints import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
  

def test_welcome_page(client):
    ans = client.get("/")
    assert "Welcome" in str(ans.data) 
    
def test_house_prc_0(client):
    ans = client.get("/0")
    assert "house_price" in str(ans.data)
    
def test_house_prc_42(client):
    ans = client.get("/42")
    assert "house_price" in str(ans.data)
    
def test_house_prc_142(client):
    ans = client.get("/142")
    assert "house_price" in str(ans.data)