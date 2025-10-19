from typing import List
from account import Account, AccountRole
from files.address import Address
from payment import PaymentMethod
from cart import Cart
from order import Order
from menu import MenuItem, Menu
from restaurant import Restaurant


class Customer(Account):
    """
    Represents a customer in the food ordering system.
    A customer can browse restaurants, view menus, manage their cart, and place orders.
    """

    def __init__(self, account_id: str, name: str, email: str, phone: str, password: str, address: Address):
        super().__init__(account_id, name, email, phone, password, AccountRole.CUSTOMER)
        self.address = address
        self.cart = Cart()
        self.payments: List[PaymentMethod] = []
        self.wallet_balance: float = 0.0

    # -------- Functional Methods --------

    def browse_restaurants(self, restaurants: List[Restaurant]):
        print("Available Restaurants:")
        for r in restaurants:
            print(f"- {r.name}")

    def view_menu(self, restaurant: Restaurant):
        print(f"Menu for {restaurant.name}:")
        for item in restaurant.menu.items:
            print(f"{item.name} - ${item.price:.2f}")

    def add_to_cart(self, menu_item: MenuItem, quantity: int):
        self.cart.add_item(menu_item, quantity)
        print(f"Added {quantity} x {menu_item.name} to your cart.")

    def add_payment_method(self, payment_method: PaymentMethod):
        self.payments.append(payment_method)
        print(f"Added new payment method: {payment_method.type}")

    def select_payment_method(self, index: int) -> PaymentMethod:
        if 0 <= index < len(self.payments):
            selected = self.payments[index]
            print(f"Selected payment method: {selected.type}")
            return selected
        else:
            print("Invalid payment selection.")
            return None

    def place_order(self, restaurant: Restaurant) -> Order:
        if not self.cart.items:
            print("Your cart is empty.")
            return None

        order = Order(customer=self, restaurant=restaurant,
                      items=self.cart.items)
        order.calculate_total()
        print(f"Order placed successfully. Total: ${order.total_price:.2f}")
        self.cart.clear_cart()
        return order
