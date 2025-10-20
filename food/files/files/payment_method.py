from enum import Enum
import uuid


class PaymentMethodType(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    APPLE_PAY = "Apple Pay"
    GOOGLE_PAY = "Google Pay"
    PAYPAL = "PayPal"
    CASH_ON_DELIVERY = "Cash on Delivery"


class PaymentMethod:
    """
    Represents a customer's saved payment method.

    Attributes:
        method_id (str): Unique ID for the payment method.
        method_type (PaymentMethodType): Type of payment method.
        details (str): Optional details, e.g., masked card number.
    """

    def __init__(self, method_type: PaymentMethodType, details: str = ""):
        self.method_id = str(uuid.uuid4())
        self.method_type = method_type
        self.details = details

    def __str__(self) -> str:
        return f"{self.method_type.value} ({self.details})" if self.details else self.method_type.value
