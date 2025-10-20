from enum import Enum
import uuid
from typing import Optional
from .order import Order
from .deliveryperson import DeliveryPerson


class DeliveryStatus(Enum):
    """
    Enum representing delivery progress stages.
    """
    PENDING = "Pending"
    ASSIGNED = "Assigned"
    PICKED_UP = "Picked Up"
    ON_ROUTE = "On Route"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class Delivery:
    """
    Represents the delivery of an order.

    Attributes:
        delivery_id (str): ID for the delivery.
        order (Order): The order to be delivered.
        delivery_person (DeliveryPerson): The person assigned to deliver.
        address (str): Destination address.
        status (DeliveryStatus): Current delivery status.
    """

    def __init__(self, order: Order, address: str):
        self.delivery_id = str(uuid.uuid4())
        self.order = order
        self.address = address
        self.delivery_person: Optional[DeliveryPerson] = None
        self.status = DeliveryStatus.PENDING

    def assign_driver(self, driver: DeliveryPerson):
        """
        Assigns a delivery person to this delivery.
        """
        self.delivery_person = driver
        self.status = DeliveryStatus.ASSIGNED
        print(
            f"Driver {driver.name} assigned to delivery {self.delivery_id}.")

    def update_status(self, new_status: DeliveryStatus):
        """
        Updates the delivery status.
        """
        self.status = new_status
        print(
            f"Delivery {self.delivery_id} status updated to: {self.status.value}.")
