def test_index(welcome_client, welcome_urls):
    response = welcome_client.get(welcome_urls['index'])
    response.status_code == 200


def test_about(welcome_urls, welcome_client):
    response = welcome_client.get(welcome_urls['about'])
    response.status_code == 200


def test_contact(welcome_urls, welcome_client):
    response = welcome_client.get(welcome_urls['contact'])
    response.status_code == 200


def test_menu(welcome_urls, welcome_client):
    response = welcome_client.get(welcome_urls['menu'])
    response.status_code == 200
