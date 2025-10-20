from enum import Enum
import uuid
from .order import Order
from .payment_method import PaymentMethod


class PaymentStatus(Enum):
    """
    different payment states.
    """
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Payment:
    """
    Represents a payment for a specific order.

    Attributes:
        payment_id (str): Unique identifier for the payment.
        order (Order): The order being paid for.
        amount (float): Payment amount.
        method (PaymentMethod): Payment method used.
        status (PaymentStatus): Current payment status.
    """

    def __init__(self, order: Order, amount: float, method: PaymentMethod):
        self.payment_id = str(uuid.uuid4())
        self.order = order
        self.amount = amount
        self.method = method
        self.status = PaymentStatus.PENDING

    def proceed_payment(self):
        """
        Simulates payment processing for the order.
        """

        pass
