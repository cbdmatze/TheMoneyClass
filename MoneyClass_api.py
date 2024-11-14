import requests

class CurrencyDownloader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        self.rates = None
   
    def update_rates(self):
        """Fetch the latest currency exchange rates."""
        reeponse = requests.get(self.base_url)
        if response.status_code == 200:
            data = response.json()
            self.rates = data['conversion_rates']
            print("Exchange rates successfully updated.")
        else:
            raise Exception("Faled to fetch currency data. Please check your API key and internet connection.")
        
    def get_rate(self, currency):
        """Return the conversion rate for a specific currency."""
        if self.rates is None:
            self.update_rates()
        return self.rates.get(currency, None)

class Money:
    currency_downloader = None # CurrencyDownloader object

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
    
