from urllib import response

def test_get_all_homepage_styles(api_client,homepage_with_multiple_styles):
    endpoint = '/api/homepage/all/'
    response = api_client().get(endpoint)
    assert response.status_code == 200