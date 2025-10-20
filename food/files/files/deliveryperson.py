from typing import List
from .account import Account, AccountRole
from .delivery import Delivery, DeliveryStatus


class DeliveryPerson(Account):
    """
    Represents a delivery driver in the system.

    Attributes:
        vehicle_id (str): The vehicle assigned to this driver.
        current_deliveries (List[Delivery]): Active deliveries.
        rating (float): Average customer rating for this driver.
    """

    def __init__(self, account_id: str, name: str, email: str, phone: str, password: str, vehicle_id: str):
        super().__init__(account_id, name, email, phone,
                         password, AccountRole.DELIVERY_PERSON)
        self.vehicle_id = vehicle_id
        self.current_deliveries: List[Delivery] = []
        self.rating: float = 5.0  # default rating

    def accept_delivery(self, delivery: Delivery):
        """
        Accepts a delivery and assigns it to this delivery person.
        """
        self.current_deliveries.append(delivery)
        delivery.assign_driver(self)
        print(f"{self.name} accepted delivery {delivery.delivery_id}.")

    def update_delivery_status(self, delivery: Delivery, new_status: DeliveryStatus):
        """
        Updates the delivery status for one of this driver's deliveries.
        """
        if delivery not in self.current_deliveries:
            print(
                f"Delivery {delivery.delivery_id} not found in {self.name}'s active list.")
            return

        delivery.update_status(new_status)
        print(
            f"{self.name} updated delivery {delivery.delivery_id} to {new_status.value}.")

    def complete_delivery(self, delivery: Delivery):
        """
        Marks the delivery as completed and removes it from active deliveries.
        """
        if delivery in self.current_deliveries:
            delivery.update_status(DeliveryStatus.DELIVERED)
            self.current_deliveries.remove(delivery)
            print(f"{self.name} completed delivery {delivery.delivery_id}.")
        else:
            print(
                f"Cannot complete delivery {delivery.delivery_id} — not found.")
