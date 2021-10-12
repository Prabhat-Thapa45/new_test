from src.order import Order, cancel
from src.utility.constants import BQ_SIZE, STOCK, YOUR_CART


def test_cancel(order, stock):
    # initial stock or Rose
    assert STOCK[0]['quantity'] == 24
    order[0].adding_to_cart()
    order[0].update_stock()
    # after adding to cart
    assert STOCK[0]['quantity'] == 20
    cancel()
    # after order being canceled it's back to initial
    assert STOCK[0]['quantity'] == 24
    assert YOUR_CART == []


class TestOrders:
    def test_flower_out_of_stock(self, order):
        assert not order[0].flower_out_of_stock()
        assert order[1].flower_out_of_stock()

    def test_bq_size_exceeded(self, order):
        # BQ_SIZE = 0, order quantity = 4
        assert order[0].bq_size_exceeded()
        BQ_SIZE[0] = 4
        assert not order[0].bq_size_exceeded()

    def test_adding_to_cart(self, order):
        BQ_SIZE[0] == 4
        assert len(order[0].adding_to_cart()) == 1
        # ordered quantity is 4 so BQ_SIZE got reduced by 4
        assert BQ_SIZE[0] == 0
        YOUR_CART.clear()

    def test_update_stock(self, order):
        # before update
        assert STOCK[0]['quantity'] == 24
        assert order[0].update_stock() == 20

    def test_check_order_criteria(self):
        assert Order.check_order_criteria()
        BQ_SIZE[0] = 1
        assert not Order.check_order_criteria()

    def test_proceed_to_buy(self):
        # clears items from your cart once the order is placed
        assert YOUR_CART == []






