"""
Restaurant Module
-----------------
Represents a restaurant that can manage its menu and handle incoming orders.
"""

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
        menu (Menu): The restaurant's menu.
        orders (List[Order]): List of orders received by the restaurant.
    """

    def __init__(self, account_id: str, name: str, email: str, phone: str, password: str, restaurant_id: str):
        super().__init__(account_id, name, email, phone,
                         password, AccountRole.RESTAURANT_MANAGER)
        self.restaurant_id = restaurant_id
        self.menu = Menu()
        self.orders: List[Order] = []

    # Menu Management

    def add_menu_item(self, item: MenuItem):
        """
        Adds a new item to the restaurant's menu.
        """
        self.menu.add_item(item)
        print(f"Added menu item '{item.name}' to {self.name} menu.")

    def remove_menu_item(self, item_id: str):
        """
        Removes a menu item from the restaurant's menu.
        """
        self.menu.remove_item(item_id)
        print(f"Removed menu item with ID {item_id} from {self.name} menu.")

    def display_menu(self):
        """
        Displays the restaurant's menu.
        """
        print(f"\n--- Menu for {self.name} ---")
        self.menu.display_menu()

    # Order Management

    def accept_order(self, order: Order):
        """
        Accepts a new order from a customer.
        """
        self.orders.append(order)
        order.update_status("ACCEPTED")
        print(f" Restaurant '{self.name}' accepted order {order.order_id}.")

    def mark_order_ready(self, order: Order):
        """
        Marks the order as ready for delivery.
        """
        order.update_status("READY")
        print(
            f"Order {order.order_id} from '{self.name}' is ready for pickup.")
