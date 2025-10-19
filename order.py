from typing import List
from .customer import Customer
from .restaurant import Restaurant
from .lineitem import LineItem
import uuid


class Order:
    """
    Represents a customer's food order.

    Relationships:
        Customer (1) ---- (*) Order
        Restaurant (1) ---- (*) Order
        Order (1) ---- (*) LineItem ---- (1) MenuItem
        Order (1) ---- (1) Delivery
        Order (1) ---- (1) Payment
    """

    def __init__(self, customer: Customer, restaurant: Restaurant, items: List[LineItem] = None):
        self.order_id = str(uuid.uuid4())
        self.customer = customer
        self.restaurant = restaurant
        self.items: List[LineItem] = items if items else []
        self.status = "Pending"
        self.total_price = 0.0

    def add_item(self, line_item: LineItem):
        """
        Adds a new line item to the order.
        """
        self.items.append(line_item)
        print(
            f"Added {line_item.menu_item.name} (x{line_item.quantity}) to Order {self.order_id}.")

    def calculate_total(self) -> float:
        """
        Calculates and updates the total price of the order.
        """
        self.total_price = sum(item.calculate_subtotal()
                               for item in self.items)
        print(f"Total price: ${self.total_price:.2f}")
        return self.total_price

    def update_status(self, new_status: str):
        """
        Updates the order status.
        """
        self.status = new_status
        print(f"Order {self.order_id} status changed to: {self.status}")
