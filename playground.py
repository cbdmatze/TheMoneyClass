class Money:
    # Conversion rates (to USD)
    conversion_rates = {
        'USD': 1.0,    # Base currency
        'EUR': 0.85,   # 1 USD = 0.85 EUR
        'GBP': 0.75,   # 1 USD = 0.75 GBP
        'JPY': 110.0,  # 1 USD = 110.0 JPY
        'AUD': 1.35,   # 1 USD = 1.35 AUD
        'CAD': 1.25,   # 1 USD = 1.25 CAD
        'CHF': 0.92    # 1 USD = 0.92 CHF
    }

    def __init__(self, amount, currency):
        if currency not in Money.conversion_rates:
            raise ValueError(f"Unsupported currency: {currency}")
        self.amount = amount
        self.currency = currency

    # Convert to another currency
    def convert_to(self, new_currency):
        if new_currency not in Money.conversion_rates:
            raise ValueError(f"Unsupported currency: {new_currency}")
        # Convert amount to USD first, then to the new currency
        amount_in_usd = self.amount / Money.conversion_rates[self.currency]
        converted_amount = amount_in_usd * Money.conversion_rates[new_currency]
        return Money(round(converted_amount, 2), new_currency)

    # Add two Money objects (even with different currencies)
    def __add__(self, other):
        if isinstance(other, Money):
            # Convert the other money to the current object's currency
            other_converted = other.convert_to(self.currency)
            new_amount = self.amount + other_converted.amount
            return Money(round(new_amount, 2), self.currency)
        elif isinstance(other, (int, float)):
            new_amount = self.amount + other
            return Money(round(new_amount, 2), self.currency)
        else:
            raise TypeError(f"Cannot add Money and {type(other)}")

    # Multiply Money by a number
    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            raise TypeError(f"Cannot multiply Money by {type(factor)}")
        new_amount = self.amount * factor
        return Money(round(new_amount, 2), self.currency)

    # Support reversed multiplication (e.g., 2 * Money)
    def __rmul__(self, factor):
        return self.__mul__(factor)

    # String representation for printing
    def __str__(self):
        return f"{self.amount} {self.currency}"

# Example usage
if __name__ == "__main__":
    # Create an instance of Money
    money1 = Money(50, 'USD')

    # Add a number to the Money object
    money2 = money1 + 50   # Now money2 should contain 100 USD
    print(money2)          # Output: 100 USD

    # Convert USD to EUR
    print(money2.convert_to('EUR'))  # This should print around 85 EUR

    # Create another instance of Money in GBP
    money3 = Money(50, 'GBP')

    # Add two instances of Money
    money4 = money2 + money3  # This should create a new Money object with around 160 USD
    print(money4)             # Output: around 160 USD

    # Multiply money by a number
    money5 = money4 * 2       # Double the amount in USD
    print(money5)             # Output: around 320 USD

    # Multiply in reverse
    money6 = 3 * money4       # Tripling the amount
    print(money6)             # Output: around 480 USD