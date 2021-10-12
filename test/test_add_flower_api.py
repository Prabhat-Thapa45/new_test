import pytest
from src.utility.constants import STOCK


@pytest.fixture()
def invalid_data_1():
    return [-1, 0, "str"]


@pytest.fixture()
def invalid_data_2():
    return [("a", "sd"), (0, 0), (-1, 2)]


class TestGet:
    def test_add_flower(self, add_client, add_urls):
        url = add_urls['add_flower']
        response = add_client.get(url)
        assert response.status_code == 200

    def test_add_new_flower(self, add_client, add_urls):
        url = add_urls['add_new_flower']
        response = add_client.get(url)
        assert response.status_code == 200


class TestPost:
    def test_add_flower(self, add_client, add_urls):
        url = add_urls['add_flower']
        response = add_client.post(url, data={'number': 4, 'flower_name': 'Rose'})
        # redirect is done to refresh the page so status code is 302
        assert response.status_code == 302
        assert response.request.path == url
        assert STOCK[0]['quantity'] == 24

    def test_add_flower_negative(self, add_client, add_urls, invalid_data_1):
        url = add_urls['add_flower']
        for i in invalid_data_1:
            response = add_client.post(url, data={'number': i, 'flower_name': 'Rose'})
            assert response.status_code == 302
            try:
                assert STOCK[0]['quantity'] != 20 + i
            except TypeError:
                pass

    def test_add_new_flower(self, add_client, add_urls):
        url = add_urls['add_new_flower']
        assert len(STOCK) == 2
        response = add_client.post(url, data={'flower_name': 'Orchid', 'quantity': '20', 'price': '4.5'})
        assert response.status_code == 302
        assert len(STOCK) == 3

    def test_add_new_flower_negative(self, add_client, add_urls, invalid_data_2):
        url = add_urls['add_new_flower']
        length = len(STOCK)
        for i, j in invalid_data_2:
            response = add_client.post(url, data={'flower_name': 'Orchid', 'quantity': i, 'price': j})
            assert response.status_code == 200
            # shows that no new items are added
            assert len(STOCK) == length
