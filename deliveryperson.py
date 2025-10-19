from .user import User
from .delivery import Delivery


class DeliveryPerson(User):
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

    def __init__(self, user_id: str, name: str, email: str, phone: str, password: str, vehicle_id: str):
        super().__init__(user_id, name, email, phone, password)
        self.vehicle_id = vehicle_id
        self.current_orders: list[Delivery] = []

    def accept_delivery(self, delivery: Delivery):

        self.current_orders.append(delivery)
        delivery.assign_driver(self)  # 调用Delivery的方法
        print(f"{self.name} accepted delivery {delivery.delivery_id}")

    def update_status(self, delivery: Delivery, new_status: str):

        delivery.update_status(new_status)
        print(f"{self.name} updated delivery {delivery.delivery_id} to {new_status}")
