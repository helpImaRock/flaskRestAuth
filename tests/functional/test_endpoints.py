from flask import Response


def check_well_formed_reply(response):
    assert type(response) == Response
    assert response.content_type == 'application/json'
    assert response.is_json == True

def test_endpoint_login_success(test_client):
    ## endpoint '/accounts/login' POST
    pass

def test_endpoint_login_failure(test_client):
    ## endpoint '/accounts/login' POST
    pass

def test_endpoint_registration_success(test_client):
    ## endpoint '/registration'
    pass

def test_endpoint_registration_failure(test_client):
    ## endpoint '/registration'
    pass

def test_endpoint_non_existing(test_client):
    response = test_client.get('/')
    check_well_formed_reply(response)
    assert response.status_code == 404
    assert response.get_json()['description'] == """The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."""
    assert response.get_json()['name'] == 'Not Found'
