from .menuitem import MenuItem


class LineItem:
    """
    Represents a single purchasable item (menu item + quantity + subtotal).
    Used in both Cart and Order.

    Attributes:
        menu_item (MenuItem): The menu item being purchased.
        quantity (int): Number of units.
        subtotal (float): Total cost for this line.

    Methods:
        calculate_subtotal(): Calculates subtotal = price * quantity.
    Relationships:
        LineItem (1) ---- (1) MenuItem
    """

    def __init__(self, menu_item: MenuItem, quantity: int):
        self.menu_item = menu_item
        self.quantity = quantity
        self.subtotal = 0.0

    def calculate_subtotal(self) -> float:
        """
        Calculates and returns the subtotal for this line.
        """
        self.subtotal = self.menu_item.price * self.quantity
        return self.subtotal

    def __str__(self) -> str:
        """
        Returns a formatted string representation of this line.
        """
        return f"{self.menu_item.name} x {self.quantity} = ${self.calculate_subtotal():.2f}"
