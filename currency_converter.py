import locale
import requests

# Request a free API key from https://exchangeratesapi.io/#pricing_plan
api_key = "db7748b38694140528d7e7674d28a765"
endpoint = "latest"


def success_call():
    response = requests.get(f'http://api.exchangeratesapi.io/v1/{endpoint}?access_key={api_key}')
    return response.json()


def rates():
    currency_rates = success_call()["rates"]
    currencies = list(currency_rates.keys())
    return currencies


def convert(conversion_currency, amount):
    currency_rate = success_call()["rates"]
    currency_rate = currency_rate[conversion_currency]
    total_amount = round(amount * currency_rate)
    return locale.currency(total_amount, grouping=True)


def check_in_list(string):
    while string not in rates():
        print("This currency doesn't exist. Check the list and try again.")
        string = input("What currency do you want to convert Euros(€) to?: ").upper()
    return string


def get_valid_amount():
    while True:
        amount_input = input(f"How much Euros would you like to convert?: ")
        try:
            amount = float(amount_input)
            return amount
        except ValueError:
            print("Please enter a valid number.")


def main_function():
    conversion_currency = input("What currency do you want to convert Euros(€) to?: ").upper()
    conversion_currency = check_in_list(conversion_currency)

    amount = get_valid_amount()
    conversion = f"Your total in {conversion_currency} would be rounded to {convert(conversion_currency, amount)}"
    print(conversion)


locale.setlocale(locale.LC_ALL, 'be_BE')  # Set the locale for proper number formatting
print(*rates(), sep="\n")
main_function()
