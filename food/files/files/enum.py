from enum import Enum


class AccountRole(Enum):
    CUSTOMER = "Customer"
    DELIVERY_PERSON = "DeliveryPerson"
    RESTAURANT_MANAGER = "RestaurantManager"


class OrderStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    READY = "Ready"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"


class DeliveryStatus(Enum):
    ASSIGNED = "Assigned"
    PICKED_UP = "PickedUp"
    DELIVERED = "Delivered"
