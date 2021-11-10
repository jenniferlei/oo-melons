"""Classes for melon orders."""

import random
import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False
    

    def get_base_price(self):
        """Calculate the base price for the melons"""

        # Price increases $4 8-11am, Monday-Friday
        # Splurge rate
        base_price = random.randrange(5, 10)

        now = datetime.datetime.now()

        # Is it rush hour?
        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4

        return base_price




    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total
    

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Ubermelon has struck a deal with the US Government. Each order will need to pass a security inspection."""

    def __init__(self, species, qty, passed_inspection):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "government", 0.0)
        self.passed_inspection = False

    
    def mark_inspection(self, passed):
        self.passed_inspection = passed


