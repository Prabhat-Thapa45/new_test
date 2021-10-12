""" this module tests welcome_api.py """


def test_index(welcome_client, welcome_urls):
    response = welcome_client.get(welcome_urls['index'])
    assert response.status_code == 200


def test_about(welcome_urls, welcome_client):
    response = welcome_client.get(welcome_urls['about'])
    assert response.status_code == 200


def test_contact(welcome_urls, welcome_client):
    response = welcome_client.get(welcome_urls['contact'])
    assert response.status_code == 200


def test_menu(welcome_urls, welcome_client):
    response = welcome_client.get(welcome_urls['menu'])
    assert response.status_code == 200
