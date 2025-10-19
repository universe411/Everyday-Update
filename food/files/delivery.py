from .order import Order
from .deliveryperson import DeliveryPerson
import uuid


class Delivery:
    """
Delivery
delivery_id
order: Order
delivery_person: DeliveryPerson
address
status
        Methods
assign_driver(driver)
update_status

    """

    def __init__(self, order: Order, address: str):
        self.delivery_id = str(uuid.uuid4())
        self.order = order
        self.address = address
        self.delivery_person = None
        self.status = "Pending"

    def assign_driver(self, driver: DeliveryPerson):

        self.delivery_person = driver
        print(f"Driver {driver.name} assigned to delivery {self.delivery_id}")

    def update_status(self, new_status: str):
        self.status = new_status
        print(f"Delivery {self.delivery_id} status changed to: {self.status}")
