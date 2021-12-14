
price_list = [911.69, 418.36, 284.92, 661.48, 99, 708.32, 402.02, 203.68, 54, 44.43, 156.26, 610.98, 621.76, 434, 350.63,
              169.51, 213.97, 777, 29.01, 558.08]

list_of_prices = []
for item in price_list:
    if type(item) is int:
        item = float(item)
    ruble, penny = map(int, str(item).split('.'))
    value_of_price = f'{ruble} руб {penny:02d} коп'
    list_of_prices.append(value_of_price)
print(', '.join(list_of_prices))

price_list.sort()
print(f'Список цен по возрастанию {price_list}, ID списка = {id(price_list)}')
price_list.sort(reverse=True)
print(f'Список цен по убыванию    {price_list}, ID списка = {id(price_list)}')
print(f'Цены 5 самых дорогих товаров: {price_list[:5]}')
