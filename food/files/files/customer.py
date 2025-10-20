from typing import List, Optional
from .account import Account, AccountRole
from .address import Address
from .payment import PaymentMethod
from .cart import Cart
from .order import Order
from .menu import MenuItem
from .restaurant import Restaurant


class Customer(Account):
    """
    Represents a customer in the system who can browse restaurants,
    view menus, add items to cart, manage payment methods, and place orders.
    """

    def __init__(self, account_id: str, name: str, email: str, phone: str, password: str, address: Address):
        super().__init__(account_id, name, email, phone, password, AccountRole.CUSTOMER)
        self.address = address
        self.cart = Cart()
        self.payment_methods: List[PaymentMethod] = []
        self.wallet_balance: float = 0.0
        self.order_history: List[Order] = []

    # Restaurant Browsing

    def browse_restaurants(self, restaurants: List[Restaurant]):
        """
        Displays a list of available restaurants.
        """
        print("Available Restaurants:")
        for r in restaurants:
            print(f"- {r.name}")

    def view_menu(self, restaurant: Restaurant):
        """
        Displays the menu for a given restaurant.
        """
        print(f"\nMenu for {restaurant.name}:")
        restaurant.menu.display_menu()

    # Cart Management

    def add_to_cart(self, menu_item: MenuItem, quantity: int):
        """
        Adds a menu item to the cart.
        """
        self.cart.add_item(menu_item, quantity)
        print(f"Added {quantity} x {menu_item.name} to your cart.")

    def view_cart(self):
        """
        Displays all items currently in the cart.
        """
        print("\nYour Cart:")
        if not self.cart.items:
            print("Cart is empty.")
        else:
            for item in self.cart.items:
                print(f"- {item}")
            self.cart.calculate_total()

    # Payment Management

    def add_payment_method(self, payment_method: PaymentMethod):
        """
        Adds a new payment method for the customer.
        """
        self.payment_methods.append(payment_method)
        print(f"Added new payment method: {payment_method.method_type.value}")

    def select_payment_method(self, index: int) -> Optional[PaymentMethod]:
        """
        Selects a payment method from the customer's saved list.
        """
        if 0 <= index < len(self.payment_methods):
            selected = self.payment_methods[index]
            print(f"Selected payment method: {selected.method_type.value}")
            return selected
        else:
            print("Invalid payment selection.")
            return None

    # Order Management

    def place_order(self, restaurant: Restaurant) -> Optional[Order]:
        """
        Places an order for all items currently in the cart.
        """
        if not self.cart.items:
            print("Your cart is empty.")
            return None

        order = Order(customer=self, restaurant=restaurant,
                      items=self.cart.items)
        order.calculate_total()
        self.order_history.append(order)

        print(f"Order placed successfully. Total: ${order.total_price:.2f}")
        self.cart.clear_cart()
        return order
