from src.utility.constants import BQ_SIZE, YOUR_CART


def test_get_bouquet_size(order_client, order_urls):
    url = order_urls['bouquet_size']

    response = order_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


class TestPost:
    def test_post_bouquet_size(self, order_client, order_urls):
        url = order_urls['bouquet_size']
        for i in [1, 3, 6]:
            response = order_client.post(url, data={'bouquet_size': i})
            assert response.status_code == 200
            assert response.request.path == url
            assert BQ_SIZE == [i]

    def test_post_bouquet_size_negative(self, order_client, order_urls):
        url = order_urls['bouquet_size']
        for i in [0, -1, 'w']:
            response = order_client.post(url, data={'bouquet_size': i})
            assert response.status_code == 422
            assert response.request.path == url

    def test_post_add_to_cart(self, order_client, order_urls):
        url = order_urls['add_to_cart']
        # giving bouquet size of 4
        order_client.post(url, data={'bouquet_size': 4})
        response = order_client.post(url, data={'number': 2, 'flower_name': 'Rose', 'price': 2.20, 'in_stock': 10})
        assert response.status_code == 200
        assert response.request.path == '/menu/bouquet_size/add'

    def test_post_add_to_cart_negative(self, order_client, order_urls):
        url = order_urls['add_to_cart']
        # giving bouquet size of 4
        order_client.post(url, data={'bouquet_size': 4})
        for i in ['h', 6, -2]:
            response = order_client.post(url, data={'number': i, 'flower_name': 'Rose', 'price': 2.20,
                                              'in_stock': 10}
                                   )
            assert response.status_code == 422
            assert response.request.path == url

    def test_go_to_cart(self, order_client, order_urls):
        url = order_urls['got_to_cart']
        response = order_client.post(url)
        assert response.status_code == 200
        assert response.request.path == url

    def test_cancel_order(self, order_client, order_urls):
        url = order_urls['cancel']
        response = order_client.post(url)
        assert response.status_code == 200
        assert len(YOUR_CART) == 0
        assert response.request.path == url

    def test_buy(self, order_client, order_urls):
        url = order_urls['buy']
        response = order_client.post(url)
        assert response.status_code == 200
        assert response.request.path == url
