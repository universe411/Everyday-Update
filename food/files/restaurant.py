from typing import List
from .account import Account, AccountRole
from .menu import Menu
from .menuitem import MenuItem
from .order import Order


class Restaurant(Account):
    """
    Represents a restaurant in the food ordering system.

    Attributes:
        restaurant_id (str): Unique ID of the restaurant.
        name (str): Restaurant name.
        menu (Menu): The restaurant's menu.
        orders (List[Order]): Orders received by the restaurant.

    Relationships:
        Restaurant (1) → (1) Menu → (*) MenuItem
        Restaurant (1) → (*) Order
    """

    def __init__(self, account_id: str, name: str, email: str, phone: str, password: str, restaurant_id: str):
        super().__init__(account_id, name, email, phone,
                         password, AccountRole.RESTAURANT_MANAGER)
        self.restaurant_id = restaurant_id
        self.menu = Menu()
        self.orders: List[Order] = []

    def add_menu_item(self, item: MenuItem):
        """
        Adds a new item to the restaurant's menu.
        """
        self.menu.add_item(item)

    def remove_menu_item(self, item_id: str):
        """
        Removes a menu item from the restaurant's menu.
        """
        self.menu.remove_item(item_id)

    def accept_order(self, order: Order):
        """
        Accepts a new order from a customer.
        """
        self.orders.append(order)
        print(f"Restaurant '{self.name}' accepted order {order.order_id}.")

    def mark_order_ready(self, order: Order):
        """
        Marks the order as ready for delivery.
        """
        order.update_status("READY")
        print(f"Order {order.order_id} is ready for pickup.")
