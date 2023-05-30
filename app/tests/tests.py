import pytest
import requests

@pytest.mark.skip('Temporary skipped')
def test_answer():
    response = requests.get('https://google.com')
    assert response.status_code == 200

def test_get_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_rate_list(client):
    response = client.get('/currency/rate/list')
    assert response.status_code == 200

def test_get_rate_list(client):
    response = client.get('/auth/login/')
    assert response.status_code == 200

def test_get_signup(client):
    response = client.get('/account/signup/')
    assert response.status_code == 200


