import requests

class CurrencyDownloader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        self.rates = None
   
    def update_rates(self):
        """Fetch the latest currency exchange rates."""
        response = requests.get(self.base_url)
        if response.status_code == 200:
            data = response.json()
            self.rates = data['conversion_rates']
            print("Exchange rates successfully updated.")
        else:
            raise Exception("Failed to fetch currency data. Please check your API key and internet connection.")
        
    def get_rate(self, currency):
        """Return the conversion rate for a specific currency."""
        if self.rates is None:
            self.update_rates()
        rate = self.rates.get(currency, None)
        if rate is None:
            raise ValueError(f"Unsupported or unknown currency: {currency}")
        return rate

class Money:
    currency_downloader = None  # CurrencyDownloader object

    def __init__(self, amount, currency):
        if Money.currency_downloader is None:
            raise ValueError("CurrencyDownloader must be initialized.")
        if currency not in Money.currency_downloader.rates:
            raise ValueError(f"Unsupported currency: {currency}")
        self.amount = amount
        self.currency = currency
    
    @classmethod
    def set_currency_downloader(cls, downloader):
        """Set the currency downloader for all Money instances."""
        cls.currency_downloader = downloader
    
    # Convert to another currency
    def convert_to(self, new_currency):
        if new_currency == self.currency:
            return Money(self.amount, self.currency)  # No conversion needed
        if new_currency not in Money.currency_downloader.rates:
            raise ValueError(f"Unsupported currency: {new_currency}")
        # Get the real-time conversion rate
        rate_to_usd = Money.currency_downloader.get_rate(self.currency)
        rate_to_new_currency = Money.currency_downloader.get_rate(new_currency)
        # Convert amount to USD first then to the new currency
        amount_in_usd = self.amount / rate_to_usd
        converted_amount = amount_in_usd * rate_to_new_currency
        return Money(round(converted_amount, 2), new_currency)
    
    # Add two Money objects (even with different currencies)
    def __add__(self, other):
        if isinstance(other, Money):
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
    
    def __rmul__(self, factor):
        return self.__mul__(factor)
    
    # String representation for printing
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
# Example usage
if __name__ == "__main__":
    # Initialize the currency downloader with a valid API key
    api_key = 'your_api_key_here'  # Insert your API key here
    currency_downloader = CurrencyDownloader(api_key)
    currency_downloader.update_rates()  # Fetch live currency rates

    # Set the downloader in the Money class
    Money.set_currency_downloader(currency_downloader)

    # Create a Money instance
    money1 = Money(100, 'USD')
    print(money1)  # Should print "100 USD"

    # Convert USD to EUR
    money2 = money1.convert_to('EUR')
    print(money2)  # Should print the converted amount in EUR

    # Add two Money objects in different currencies
    money3 = Money(50, 'GBP')
    money4 = money1 + money3
    print(money4)  # Should print the total in USD after conversion
