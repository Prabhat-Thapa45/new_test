"""
processes requests from api to take orders
"""
from typing import Tuple, Union
from src.utility.constants import BQ_SIZE, STOCK, YOUR_CART


def cancel() -> None:
    """
    cancels order, updates the stock and clears YOUR_CART
    """
    for item_1 in YOUR_CART:
        for item_2 in STOCK:
            if item_1["flower_name"] == item_2["flower_name"]:
                item_2["quantity"] += item_1["quantity"]
                break
    YOUR_CART.clear()


class Order:
    """
    Helps in taking order
    """

    def __init__(self, valid_order_quantity, in_stock, flower_name, price):
        self.valid_order_quantity = valid_order_quantity
        self.in_stock = in_stock
        self.flower_name = flower_name
        self.price = price

    def flower_out_of_stock(self) -> bool:
        """
        Checks if flower is in stock or not
        :return: True if out of stock else False
        """
        if self.valid_order_quantity > self.in_stock:
            return True
        else:
            return False

    def bq_size_exceeded(self) -> Union[bool, None]:
        """
        Checks if items added to cart exceeds bouquet size
        :return: True if exceeds else None
        """
        if self.valid_order_quantity > BQ_SIZE[0]:
            return True

    def adding_to_cart(self) -> Tuple[list, list]:
        """
        Adds item to your cart and reduces the bouquet size
        :return: list of items in your cart and updated bouquet size
        """
        YOUR_CART.append(
            {
                "flower_name": self.flower_name,
                "quantity": self.valid_order_quantity,
                "price": self.price,
            }
        )
        BQ_SIZE[0] -= self.valid_order_quantity
        return YOUR_CART

    def update_stock(self) -> int:
        """
        reduces quantity from stock after purchase
        :return: updated quantity
        """
        for item in STOCK:
            if item["flower_name"] == self.flower_name:
                item["quantity"] -= self.valid_order_quantity
                return item["quantity"]

    @staticmethod
    def check_order_criteria() -> True:
        """
        checks if bouquet size == 0
        :return: True if it is 0
        """
        if BQ_SIZE[0] == 0:
            return True

    @staticmethod
    def proceed_to_buy() -> str:
        """
        Clears items from your cart
        :return: success message
        """
        YOUR_CART.clear()
        return "Order placed successfully"
