class Address:
    """
    Represents a physical address used by customers and deliveries.
    """

    def __init__(self, street: str, city: str, zipcode: str, country: str):
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.country = country

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the address.
        """
        return f"{self.street}, {self.city}, {self.zipcode}, {self.country}"

    def to_dict(self) -> dict:
        """
        Converts the address into a dictionary (useful for JSON serialization or database storage).
        """
        return {
            "street": self.street,
            "city": self.city,
            "zipcode": self.zipcode,
            "country": self.country
        }
