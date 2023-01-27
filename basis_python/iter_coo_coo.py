# Пишем итератор, который выдает заданную фразу необходимое количество раз
import sys
from random import shuffle


RANDOM_ANSWERS = [
    '-Это я, почтальон Печькин, принес заметку про вашего мальчика.',
    '-Это я, почтальон Печькин, принес журнал "Мурзилка".',
    '-ДА НИКТО!',
]


class CooCooIterator:
    def __init__(self, num_iter, phrase='-Кто там?'):
        self.counter = 0
        self.num_iter = num_iter
        self.phrase = phrase

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num_iter:
            self.counter += 1
            return self.phrase
        raise StopIteration


num_iter = int(sys.stdin.readline().strip())
greeter = CooCooIterator(num_iter)

for i in greeter:
    shuffle(RANDOM_ANSWERS)
    print('-Тук-тук.')
    print(i)
    print(f'{RANDOM_ANSWERS[0]}', end='\n\n')
