from datetime import date
from decimal import Decimal
import requests


def get_currency_rate(currency_code='USD'):
    currency_code = currency_code.upper()
    response_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_starts_at_index = response_text.find(currency_code)
    if currency_starts_at_index == -1:
        return

    date_index = response_text.find('Date')

    currency_date = response_text[date_index + 6:date_index + 16]
    day, month, year = (int(x) for x in currency_date.split('.'))
    refined_currency_date = date(year,month,day)

    nominal = getField('<Nominal>', response_text, currency_starts_at_index)
    currency_price = \
        getField('<Value>', response_text, currency_starts_at_index)
    currency_price = currency_price.replace(',','.')
    return f'На {refined_currency_date} {nominal} {currency_code} == ' \
            f'{Decimal(currency_price)} RUR'

def getField(field_name, response_text,currency_start_at_index):
    value_start_index = response_text.find(field_name, currency_start_at_index) + len(field_name)
    value_end_index = response_text.find('</', value_start_index)
    return response_text[value_start_index:value_end_index]


print(get_currency_rate())
