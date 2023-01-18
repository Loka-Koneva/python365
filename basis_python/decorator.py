# Все, включая функции, является объектами в Питоне
# По синтаксису, декоратор - это функция, которая принимает в качестве аргумента др.функцию
# По сути, декоратор - это обертка над функцией, которая расширяет функционал последней

# 1) Введение в декораторы

def my_shiny_decorator(func_to_decorated):
    def the_wrapper_around_original_func():
        print('Код до вызова функции')
        func_to_decorated()
        print('Код после вызова функции', end='\n\n')
    return the_wrapper_around_original_func


def standart_alone_func():
    print('Я старая, почтенная, неизменяемая функция!')

# Первый вариант записи
standart_alone_func = my_shiny_decorator(standart_alone_func)
standart_alone_func()


# Второй вариант записи. Использован синтаксис декораторов.
@my_shiny_decorator
def another_standart_alone_func():
    print('Другая почтенная функция!')


another_standart_alone_func()

# Декоратор для функции с аргументами. Передаем аргументы в обертку, а она их в функцию

def decorator_passing_args(func_to_decorate):
    def wrapper_accepting_args(arg1, arg2):
        print(f'Посмотрим, что я получил: {arg1}, {arg2}')
        func_to_decorate(arg1, arg2)
    return wrapper_accepting_args


@decorator_passing_args
def print_full_name(first_name, last_name):
    print(f'{first_name} {last_name}', end='\n\n')


print_full_name('Ваня', 'Иванов')


# Декорирование методов
# Их главное отличие от функций в том, что первым параметром они ожидают ссылку на объект - self
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie += 3
        method_to_decorate(self, lie)
    return wrapper


class Lizy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print(f'Мне {self.age - lie} лет. А ты сколько дашь?', end='\n\n')

l = Lizy()
l.say_your_age(2)


# Декоратор, подходящий для функций и методов
def decorator_passing_arbitrary_args(any_func):
    def wrapper(*args, **kwargs):
        print('Что там мне передали??')
        print(args)
        print(kwargs)
        any_func(*args, **kwargs)

    return wrapper


@decorator_passing_arbitrary_args
def f_without_args():
    print('Здесь нет аргументов', end='\n\n')


@decorator_passing_arbitrary_args
def f_with_args(a, b, c):
    print(a, b, c, end='\n\n')


@decorator_passing_arbitrary_args
def f_with_named_args(a, b, phrase='Почему нет'):
    print(f'{a}, {b}, мы поедем отдыхать?')
    print(phrase, end='\n\n')


class Mary:
    def __init__(self):
        self.age = 16

    @decorator_passing_arbitrary_args
    def say_your_age(self, lie):
        print(f'Мне уже {self.age + lie} лет!', end='\n\n')


f_without_args()
f_with_args(1, 2, 3)
f_with_named_args('Петров', 'Васечкий', phrase='Определенно!')
m = Mary()
m.say_your_age(3)
