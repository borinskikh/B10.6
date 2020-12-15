import json
import requests


class APIException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Price:

    @staticmethod
    def get_rates():
        try:
            rates = requests.get(
                'https://api.exchangeratesapi.io/latest').json()['rates']
            rates['EUR'] = 1.00
        except:
            raise APIException("Couldn't get exchange rates")
        return rates

    @staticmethod
    def get_price(base, quote, amount):
        rates = Price.get_rates()
        if not base.isalpha() or not quote.isalpha() or not amount.isdigit():
            raise APIException('Wrong formatting')
        base = base.upper()
        quote = quote.upper()
        if base not in rates:
            raise APIException(
                base + ' is not in the available exchange rates')
        if quote not in rates:
            raise APIException(
                quote + ' is not in the available exchange rates')
        price = round(float(amount) *
                      rates[quote] / rates[base], 2)
        output = str(amount)+" "+base+" = "+str(price)+" "+quote
        return output
