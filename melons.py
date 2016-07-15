"""This file should have our order classes in it."""

from random import randint
import datetime


class AbstractMelonOrder(object):
    """The base class for melon orders, both international and domestic"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.current_date = datetime.datetime.today().weekday()
        self.order_hour = datetime.datetime.now().time().hour



    def get_base_price(self):
        """Generates current base price from random int between 5-9"""

        random_base = randint(5,9)

        if self.current_date in range(0, 5) and self.order_hour in range(8, 12):
            random_base += 4.00

        return random_base

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return round(total, 4)


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

    # def get_total(self):
    #     """Calculate price."""

    #     return super(DomesticMelonOrder, self).get_total()


    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     return super(DomesticMelonOrder, self).mark_shipped()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price."""

        intl_total = super(InternationalMelonOrder, self).get_total()

        if self.quantity < 10:
            intl_total += 3.00

        return intl_total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     return super(InternationalMelonOrder, self).mark_shipped()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Class for government orders with zero tax"""

    def __init__(self, species, qty):
        """All government orders have zero tax and will return True if passed through an inspection"""

        super(GovernmentMelonOrder, self).__init__(species, qty)

        self.tax = 0.0
        self.order_type = "domestic"
        self.passed_inspection = False


    def mark_inspection(self, passed=True):
        """Updates passed inspection to true"""

        self.passed_inspection = passed
