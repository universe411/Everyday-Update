from enum import Enum


class AccountRole(Enum):
    CUSTOMER = "Customer"
    DELIVERY_PERSON = "DeliveryPerson"
    RESTAURANT_MANAGER = "RestaurantManager"


class Account:
    """
    represents a system account that can log in and out.
    Each account belong to a customer, delivery person, or restaurant manager.
    """

    def __init__(self, account_id: str, name: str, email: str, phone: str, password: str, role: AccountRole):
        self.account_id = account_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.role = role
        self.is_logged_in = False

    def login(self, email: str, password: str) -> bool:
        """
        Authenticates the user by checking email and password.
        Returns True if login succeeds, False otherwise.
        """
        if self.email == email and self.password == password:
            self.is_logged_in = True
            print(f"{self.name} logged in successfully as {self.role.value}.")
            return True
        else:
            print("Invalid email or password.")
            return False

    def logout(self):
        """
        Logs out the user if currently logged in.
        """
        if self.is_logged_in:
            self.is_logged_in = False
            print(f"{self.name} logged out.")
        else:
            print(f"{self.name} is not logged in.")
