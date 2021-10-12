""" this module tests add_flower.py """

from src.utility.constants import STOCK


def test_add_to_stock(add):
    assert STOCK[0]['quantity'] == 20
    add[0].add_to_stock(10)
    assert STOCK[0]['quantity'] == 30
    STOCK[0]['quantity'] = 20


def test_add_new_in_stock(add):
    length = len(STOCK)
    add[1].add_new_in_stock(10, 4.5)
    assert len(STOCK) == length + 1
    STOCK.pop()

