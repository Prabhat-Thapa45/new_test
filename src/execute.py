from src.utility.constants import STOCK, BQ_SIZE, YOUR_CART
from src.utility.validate_input import validate_int
from src.order import Order


def find_flower_details(flower_name):
    for item in STOCK:
        if item['flower_name'] == flower_name:
            return item['quantity'], item['price']


def get_int_input():
    amount = input("Enter positive integer")
    while True:
        valid_input = validate_int(amount)
        if not valid_input:
            amount = input("please enter valid integer for bouquet size")
        else:
            return amount


def execute_order():
    print("Enter bouquet size")
    BQ_SIZE[0] = get_int_input()
    print("Enter order quantity")
    valid_order_quantity = get_int_input()
    flower_name = input("Enter flower name")
    in_stock, price = find_flower_details(flower_name)
    order = Order(valid_order_quantity, in_stock, flower_name, price)
    if order.flower_out_of_stock():
        print("We are running low on this flower")
        response = input("Do you want to look for alternative? Y/N")
        if response.upper() == 'N':
            return
