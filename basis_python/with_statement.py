# Пишем контекстный менеджер. Помним, что в принципе любой код try-except-finally можно завернуть в контекстный менеджер
# На уровне класса контекстный менеджер определяется наличием и работой магических методов __enter__, __exit__
from contextlib import contextmanager


# Создаем тестовый класс Recource
class Resource:
    def __init__(self):
        self.is_opened = False

    def open(self, *args):
        print(f'Resouce was opened with args: {args}')
        self.is_opened = True

    def close(self):
        print('Resource was closed', end='\n\n')
        self.is_opened = False

    def __del__(self):
        if self.is_opened:
            print('Memory leak detected! Resource was not closed!', end='\n\n')

    def action(self):
        print('Do something with Resource.')


# Вариант первый - при помощи библиотеки contextlib
@contextmanager
def resource_open(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource  # Самое важное!! Тут yield!!
    except:
        print('ALARM')
        raise
    finally:
        if resource:
            resource.close()


class ResourceWorker():
    def __init__(self, *args):
        self.resource = None
        self.args = args

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource  # А вот тут return!

    # При вызове исключения сюда придет его тип, значение и трейсбек
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()


with resource_open(4, 5, 6) as ro:
    print('First case')
    ro.action()

with ResourceWorker(7, 8, 9) as rw:
    print('Second case')
    rw.action()
