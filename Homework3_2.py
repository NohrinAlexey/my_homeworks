number_in_english = input('Введите число от 0 до 10 текстом на английском ')
nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(num):
    """ Функция возвращает перевод на русский введенного названия числа на английском
    Если название введено с заглавной буквы, то и результат будет выведен с залавной буквы

    :parameter (str) Название числа на английском от 0 до 10. Например ten, one и т.д.
    """

    if num.lower() in nums:
        if num.istitle():
            num = num.lower()
            result = nums[num].title()
            return result
        else:
            result = nums[num]
            return result
    else:
        return None


print(num_translate_adv(number_in_english))
