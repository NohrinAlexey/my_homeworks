from utils import get_currency_rate

print(get_currency_rate())
print(get_currency_rate('EUR'))
print(get_currency_rate('BYN'))

if __name__ == '__main__':
    from sys import argv
    _module_name, currency_code_arg = argv