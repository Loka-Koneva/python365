"""
Определить сумму минимальных чисел в списке
"""


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


def sum_two_smallest_numbers_2(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min


list_numbers = [14, 11, 9, 5, 6, 15]
# print(sum_two_smallest_numbers(list_numbers))
# print(sum_two_smallest_numbers_2(list_numbers))

"""
Сгенерировать все правильные скобочные последовательности со скобками одного вида

Результат проверки: 
Run-time error  RE  Да  Программа завершила работу с ненулевым кодом возврата
 
Требования к выходным данным:
Выходной файл содержит сгенерированные правильные скобочные последовательности, 
упорядоченные лексикографически
"""

import sys
import numpy as np

# k = 2*int(sys.stdin.readline().strip())
# init = list(np.zeros(k))
cnt = 0
ind = 0

def f(cnt, ind, k, init):
    if (cnt <= k-ind-2):
        init[ind] = '('
        f(cnt+1, ind+1, k, init)
    if cnt > 0:
        init[ind] = ')'
        f(cnt-1, ind+1, k, init)
    if ind == k:
        if cnt == 0:
            print(''.join(init))

# f(cnt, ind, k, init)

"""
Даны две строки строчных латинских символов: строка J и строка S. 
Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». 
Нужно определить, какое количество символов из S одновременно являются «драгоценностями».
Проще говоря, нужно проверить, какое количество символов из S входит в J.

Результат проверки: все тесты прошли
"""

import sys

# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()


def str_diff(J_str, S_str):
    count = 0
    for i in S_str:
        if J_str.count(i):
            count = count + 1
    return count


# print(str_diff(j, s))

"""
Требуется найти в бинарном векторе 
самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время 
и при этом проходящее по входному массиву только один раз.

Результат: частичное решение, остановка на 80 тесте
Внесла правки в уровень if. Думаю, теперь верно
"""

import sys

# len_list_number = sys.stdin.readline().strip()
# list_number = []
# for i in range(int(len_list_number)):
#     n = sys.stdin.readline().strip()
#     list_number.append(int(n))

def max_len_of_unit(list_number):
    max_len = 0
    count = 0
    coint_of_zero = 0

    for i in list_number:
        if i == 1:
            count = count+1
        else:
            if count > max_len:
                max_len = count
            coint_of_zero += 1
            count = 0
    if coint_of_zero == 0:
        max_len = count
    return max_len

# print(max_len_of_unit(list_number))

"""
Определить, являются ли 2 строчки анаграммами
"""

import sys
import collections

first_str = sys.stdin.readline().strip()
second_str = sys.stdin.readline().strip()


def diff_str_anagramm(first_str, second_str):
    if len(first_str) != len(second_str):
        return 0

    if collections.Counter(first_str) == collections.Counter(second_str):
        return 1

    return 0


print(diff_str_anagramm(first_str, second_str))







