def test_get_api_rate_list(api_client):
    response = api_client.get('/api/currency/rates/')
    assert response.status_code == 200

def test_post_api_rate_list(api_client):
    response = api_client.post('/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_get_api_sourse_list(api_client):
    response = api_client.get('/api/currency/sources/')
    assert response.status_code == 200


def test_post_api_source_list(api_client):
    response = api_client.post('/api/currency/sources/')
    assert response.status_code == 400
