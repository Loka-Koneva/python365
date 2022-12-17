"""
Создание правильной скобочной последовательности из одного вида скобок
Вариант 1 - алгоритм с очередью
"""
from queue import Queue

def generate_brackets_sequence(n):
    q = Queue()
    q.put_nowait({'str': '(', 'left_count': 1, 'right_count': 0})

    while not q.empty():
        el = q.get()
        if len(el['str']) == 2*n:
            print(el['str'])
            continue
        if el['left_count'] < n:
            q.put({
                'str': el['str'] + '(',
                'left_count': el['left_count']+1,
                'right_count': el['right_count']
            })
        if el['right_count'] < el['left_count']:
            q.put({
                'str': el['str'] + ')',
                'left_count': el['left_count'],
                'right_count': el['right_count']+1
            })


generate_brackets_sequence(1)
print('_'*40)

"""
Создание правильной скобочной последовательности из одного вида скобок
Вариант 2 - рекурсия. Рекомендовано Яндексом 
(https://www.youtube.com/watch?v=zU-LndSG5RE&ab_channel=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0)
"""

def generate(cur, open, closed, n):
    if len(cur)==2*n:
        print(cur)
        return
    if open < n:
        generate(cur+'(', open+1, closed, n)
    if closed < open:
        generate(cur+')', open, closed+1, n)

def parens(n):
    generate('', 0, 0, n)

parens(3)
