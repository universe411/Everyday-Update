from .order import Order
from enum import Enum
import uuid


class PaymentStatus(Enum):
    """
    Enum representing different payment states.
    """
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Payment:
    """
    Represents a payment for an order.
    -----------------------------------
    Attributes:
        payment_id (str): Unique identifier.
        order (Order): The related order.
        amount (float): Payment amount.
        method (PaymentMethod): Optional, the payment method used.
        status (PaymentStatus): Current payment status.

    Relationships:
        Order 1-1 Payment
    """

    def __init__(self, order: Order, amount: float):
        self.payment_id = str(uuid.uuid4())
        self.order = order
        self.amount = amount
        self.status = PaymentStatus.PENDING

    def proceed_payment(self):
        """
        process of making the payment.
        """
        pass
