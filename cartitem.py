from .menuitem import MenuItem


class CartItem:
    """
    Represents an individual item inside a Cart.
    Each CartItem links to one MenuItem and stores its quantity and subtotal.

    Relationships:
        CartItem (1) ---- (1) MenuItem
    """

    def __init__(self, menu_item: MenuItem, quantity: int):
        self.menu_item = menu_item      # MenuItem object
        self.quantity = quantity        # quantity of this menu item in cart
        self.subtotal = 0.0             # subtotal value

    def calculate_subtotal(self) -> float:
        """
        Calculates and returns the subtotal for this cart item.
        """
        self.subtotal = self.menu_item.price * self.quantity
        return self.subtotal

    def __str__(self) -> str:
        """
        Returns a human-readable summary of the cart item.
        """
        return f"{self.menu_item.name} x {self.quantity} = ${self.calculate_subtotal():.2f}"
