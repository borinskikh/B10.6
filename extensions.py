import json
import requests


class InputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Price:

    @staticmethod
    def get_price(message):
        values = message.text.split()
        rates = requests.get(
            'https://api.exchangeratesapi.io/latest').json()['rates']
        rates['EUR'] = 1.00
        if len(values) > 3:
            raise InputError('Too many arguments')
        if len(values) < 3:
            raise InputError('Not enough arguments')
        currencyFrom = values[0]
        currencyTo = values[1]
        amount = values[2]
        if not currencyFrom.isalpha() or not currencyTo.isalpha() or not amount.isdigit():
            raise InputError('Wrong format')
        currencyFrom = currencyFrom.upper()
        currencyTo = currencyTo.upper()
        if currencyFrom not in rates:
            raise InputError(currencyFrom+' is not an accepted currency')
        if currencyTo not in rates:
            raise InputError(currencyTo+' is not an accepted currency')
        price = round(float(amount) *
                      rates[currencyTo.upper()] / rates[currencyFrom.upper()], 2)

        return price
