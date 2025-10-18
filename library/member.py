class Member:
    """
    Represents a regular library member
    """

    def __init__(self, member_id: str, name: str, phone_number: str, points=50, balance=0):
        """Initialize member info and default balance."""
        self.member_id = member_id
        self.name = name
        self.phone_number = phone_number
        self.points = int(points)
        self.balance = float(balance)
        self.is_vip = False  # default to normal member

    def can_borrow_days(self) -> int:
        """Return how many days the member can borrow a book."""
        return 5

    def get_daily_fee(self) -> float:
        """Daily borrowing fee for normal members."""
        return 1.0  # $1 per day

    def recharge(self, amount: float):
        """Add money to the member’s balance."""
        self.balance += amount
        print(
            f"{self.name} recharged ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def upgrade_to_vip(self):
        """Upgrade to VIP if balance >= $50."""
        if self.balance >= 50:
            new_vip = VIPMember(
                member_id=self.member_id,
                name=self.name,
                phone_number=self.phone_number,
                points=self.points,
                balance=self.balance
            )
            print(f"{self.name} upgraded to VIP successfully!")
            return new_vip
        else:
            print(f"{self.name} has insufficient balance to upgrade (need $50).")
            return self

    def __str__(self):
        """Return a readable string of member details."""
        return (
            f"Member[{self.member_id}] {self.name} | Phone: {self.phone_number} | "
            f"Points: {self.points} | Balance: ${self.balance:.2f} | "
            f"Status: {'VIP' if self.is_vip else 'Regular'}"
        )

# vip member inherits Member


class VIPMember(Member):
    """Represents a VIP member with discounts and extended privileges."""

    def __init__(self, member_id, name, phone_number, points=100, balance=0, vip_level=1):
        """Initialize VIP member with level and balance."""
        super().__init__(member_id, name, phone_number, points, balance)
        self.vip_level = vip_level
        self.is_vip = True

    def can_borrow_days(self) -> int:
        """Return how many days the VIP can borrow a book."""
        return 30

    def get_daily_fee(self) -> float:
        """Return discounted daily fee for VIP."""
        base_fee = 1.0
        if self.vip_level == 1:
            return base_fee * 0.5  # 50% off
        elif self.vip_level == 2:
            return base_fee * 0.2  # 80% off
        else:
            return 0.0  # free for top-tier VIP

    def get_discount(self) -> float:
        """Return the purchase discount rate for VIP."""
        return 0.8 if self.vip_level == 1 else 0.5

    def __str__(self):
        """Return readable info for a VIP member."""
        return (
            f"VIPMember[{self.member_id}] {self.name} | Level: {self.vip_level} | "
            f"Points: {self.points} | Balance: ${self.balance:.2f}"
        )
