class MenuItem:
    """
    Represents a single dish or item in a restaurant's menu.

    Attributes:
        item_id (str): Unique identifier for the menu item.
        name (str): Name of the dish.
        price (float): Price of the item.
        description (str): Short description of the dish.

    Relationships:
        Menu (1) ---- (*) MenuItem
        CartItem / LineItem (1) ---- (1) MenuItem
    """

    def __init__(self, item_id: str, name: str, price: float, description: str):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        """
        Returns a human-readable string describing the menu item.
        """
        return f"{self.name} (${self.price:.2f}) - {self.description}"
