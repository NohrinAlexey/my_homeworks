def logger_type(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}:{type(arg)}')
        result = func(*args)
        return result
    return wrapper


@logger_type
def multiplication(a, b):
    return a * b


print(multiplication(2, 7))
