# Продолжаем повторять декораторы. Сейчас запишем декоратор, в кот. можно передать args

def decorator_maker(decorator_arg1, decorator_arg2):
    print(f'Я создаю декоратор и я получил аргументы: '
          f'{decorator_arg1}, {decorator_arg2}')

    def decorator(func):
        print(f'Я декоратор, при создании мне передали переменные: '
              f'{decorator_arg1}, {decorator_arg2}')

        def wrapper(func_arg1, func_arg2):
            print('Я - обертка и у меня есть доступ ко всем аргументам: ',
                  f'{decorator_arg1}, {decorator_arg2}, {func_arg1}, {func_arg2}')
            return func(func_arg1, func_arg2)
        return wrapper
    return decorator


@decorator_maker('Синий', 'Зеленый')
def some_func(func_arg1, func_arg2):
    print(f'Я - декорируемая функция. Я знаю только о своих аргументах: '
          f'{func_arg1}, {func_arg2}', end='\n\n')


some_func('Круг', 'Квадрат')


# Создаем декоратор на основе класса
class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        self.counter += 1
        print(f'Called {self.counter} times')


@MyDecorator
def my_test():
    print(42)


my_test()
my_test()
my_test()

# Пишем декоратор для оценки времени работы функции
# Т.к. рассматриваются отдельные кейсы, считаю возможным импортировать модули в середине файла

from functools import wraps
from time import perf_counter

def timer(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        runtime = perf_counter() - start
        print(f'{func.__name__} took {runtime:.4f} secs.')
        return result
    return _wrapper


# Ф-ия выводит последнюю цифру большого числа Фибоначчи
@timer
def fib_digit(n):
    fib_and_list = [0, 1, 1]
    if n <= 2:
        return fib_and_list[n]
    for i in range(3, n):
        fib_and_list.append((fib_and_list[i-1] + fib_and_list[i-2])%10)
    return (fib_and_list[n-1]+fib_and_list[n-2])%10


print('')
print(fib_digit(1241943))
