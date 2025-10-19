from typing import List
from .menuitem import MenuItem


class Menu:
    """
    Represents a restaurant's menu containing multiple menu items.

    Attributes:
        items (List[MenuItem]): A list of menu items offered by the restaurant.

    Methods:
        add_item(item): Adds a new menu item.
        remove_item(item_id): Removes an item by ID.

    Relationships:
        Menu (1) ---- (*) MenuItem
    """

    def __init__(self):
        # Initialize an empty list of menu items
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem):
        """
        Adds a new menu item to the menu.
        """
        self.items.append(item)
        print(f"Added item '{item.name}' to menu.")

    def remove_item(self, item_id: str):
        """
        Removes a menu item by its ID.
        """
        before_count = len(self.items)
        self.items = [item for item in self.items if item.item_id != item_id]
        after_count = len(self.items)

        if before_count == after_count:
            print(f"No item found with ID: {item_id}")
        else:
            print(f"Removed item with ID: {item_id}")

    def display_menu(self):
        """
        Displays all items in the menu.
        """
        if not self.items:
            print("The menu is currently empty.")
            return

        print("---- MENU ----")
        for item in self.items:
            print(f"{item.name} - ${item.price:.2f}: {item.description}")
        print("--------------")
