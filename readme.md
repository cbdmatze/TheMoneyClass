

# Money Conversion Application

## Overview

This Python program implements a `Money` class that represents money in different currencies and supports real-time conversion between them. The program relies on an external API (ExchangeRate-API) to fetch up-to-date currency exchange rates. The program can perform various operations on money such as addition, multiplication, and conversion between currencies.

## Features

- **Real-Time Currency Conversion**: The `Money` class supports conversion between seven currencies (USD, EUR, GBP, JPY, AUD, CAD, CHF) using real-time exchange rates.
- **Addition**: You can add two `Money` objects, even if they are in different currencies. The result will be in the currency of the first object.
- **Multiplication**: You can multiply a `Money` object by an integer or float.
- **Automatic Rate Updates**: The program fetches the latest exchange rates whenever required using the ExchangeRate-API.
- **Custom Currency API**: A `CurrencyDownloader` class is responsible for downloading the exchange rates from the API.

## Supported Currencies

- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- AUD (Australian Dollar)
- CAD (Canadian Dollar)
- CHF (Swiss Franc)

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library: You can install it using the following command:
  ```bash
  pip install requests

Installation

	1.	Clone the repository:

git clone <repository-url>
cd <repository-folder>


	2.	Create a Virtual Environment (Optional but recommended):

python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate


	3.	Install dependencies:
Install the requests library if you haven’t already:

pip install requests



API Key Setup

To fetch real-time exchange rates, you need an API key from ExchangeRate-API.
	1.	Go to ExchangeRate-API and sign up for a free account.
	2.	Copy the API key provided by the service.
	3.	Replace the placeholder in the script with your actual API key:

api_key = 'your_api_key_here'



Usage

	1.	Run the Script:

python3 MoneyClass_api.py


	2.	Basic Operations:
	•	Convert money between currencies:

money1 = Money(100, 'USD')
money2 = money1.convert_to('EUR')
print(money2)  # Prints the amount in EUR


	•	Add two Money objects (even in different currencies):

money3 = Money(50, 'GBP')
money4 = money1 + money3
print(money4)  # Prints the total in USD after conversion


	•	Multiply a Money object:

money5 = money1 * 2
print(money5)  # Prints "200 USD"



Notes

	•	This program uses the ExchangeRate-API free tier. Be mindful of the rate limits for API calls.
	•	The program assumes that the API key and internet connection are correctly configured to fetch exchange rates.

License

This project is licensed under the MIT License.
