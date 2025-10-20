"""
Cart Module
------------
Represents a shopping cart that holds multiple line items.
Relationships:
    Cart (1) ---- (*) LineItem
    LineItem (1) ---- (1) MenuItem
"""

from typing import List
from .lineitem import LineItem
from .menuitem import MenuItem


class Cart:
    """
    Represents a customer's shopping cart.
    """

    def __init__(self):
        # initialize the cart with an empty item list
        self.items: List[LineItem] = []

    def add_item(self, menu_item: MenuItem, quantity: int):
        """
        Adds a menu item to the cart.
        If the item already exists, increase its quantity.
        """
        for item in self.items:
            if item.menu_item == menu_item:
                item.quantity += quantity
                print(
                    f"Updated quantity of {menu_item.name} to {item.quantity}.")
                return

        # Create a new line item if not already in the cart
        new_item = LineItem(menu_item, quantity)
        self.items.append(new_item)
        print(f"Added {menu_item.name} (x{quantity}) to cart.")

    def remove_item(self, menu_item: MenuItem):
        """
        Removes a specific item from the cart.
        """
        for item in self.items:
            if item.menu_item == menu_item:
                self.items.remove(item)
                print(f"Removed {menu_item.name} from cart.")
                return
        print(f"{menu_item.name} not found in cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart.
        """
        total = sum(item.calculate_subtotal() for item in self.items)
        print(f"Total: ${total:.2f}")
        return total

    def clear_cart(self):
        """
        Clears all items from the cart.
        """
        self.items.clear()
        print("Cart has been cleared.")
