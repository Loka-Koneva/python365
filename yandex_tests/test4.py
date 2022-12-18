# Технический долг
#
# Реализация большого проекта — очень сложная задача, и при разработке программист Алексей руководствуется следующим принципом: сначала написать работающий прототип, а потом улучшать код. Чтобы не забыть, что именно отложено на потом, на каждый такой долг Алексей заводит на себя задачу в специальной системе Yagile.
#
# Система устроена следующим образом: для каждой задачи задается дедлайн — день titi​. Если задача не решена до этого момента времени, то в задачу приходит робот и пишет комментарий о том, что задачу надобно закрыть. Если через XX дней задача не решена, то робот приходит снова. Так продолжается до тех пор, пока задача не будет решена.
#
# Алексей каждый день заходит в Yagile и видит сообщения от робота. Если Алексей не хочет приступать к решению накопленных задач, то он прочитывает все сообщения с помощью одной кнопки и занимается другими делами. Однако Алексей понимает, что так долго делать нельзя, поэтому он разрешает себе нажимать на эту кнопку ровно K−1K−1 раз, а на KK-й раз садится и решает все задачи разом (даже те, у которых не настал дедлайн).
#
# Определите день, когда Алексей закроет все задачи.
# Формат ввода
#
# Первая строка содержит три целых числа NN (1≤N≤1051≤N≤105) — количество накопленных задач, XX (1≤X≤1091≤X≤109) — количество дней, через которое приходит робот и число KK из условия (1≤K≤1091≤K≤109).
#
# Вторая строка содержит NN целых чисел t1t1​, t2t2​, ……, tNtN​ (1≤ti≤1091≤ti​≤109) — дедлайны соответствующих задач.
# Формат вывода
#
# Выведите одно число — день, когда Алексей закроет все задачи.
# Пример 1
# Ввод
#
# 6 5 10
# 1 2 3 4 5 6
#
# Вывод
#
# 10
#
# Пример 2
# Ввод
#
# 5 7 12
# 5 22 17 13 8
#
# Вывод
#
# 27

# Ограничение памяти
# 256.0 Мб
# Ограничение времени
# 2 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
import sys

def f():
    dig_first = list(map(int, input().split()))
    dedline_list = list(map(int, input().split()))

    len_number = min(dedline_list)*dig_first[2]
    time_line = [0 for _ in range(len_number)]

    for day in dedline_list:
        count = day

        while count < len_number:
            print(time_line, count)
            time_line[count] = 1
            count += dig_first[1]

    count_alarm = 0
    for i in range(len_number):
        if count_alarm == dig_first[2]:
            print(i-1)
            break
        if time_line[i] == 1:
            count_alarm += 1

f()
#
# Резюмен: неверное решение. Тесты пройдены или не пройдены с ошибкой "Превышен лимит памяти".
# Также есть неверные ответы. Вероятно, не все краевые условия обработаны.

# Ввод
#
# 5 7 12
# 5 22 17 13 8
#
# Ввод
#
# 6 5 10
# 1 2 3 4 5 6
