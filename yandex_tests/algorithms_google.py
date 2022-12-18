"""
На вход подается список температур за неделю.
На выходе нужно получить список из цифр - дни до следующего более теплого дня.
Вариант 1
Два вложенных цикла
Время работы О(n^2); расход по памяти О(n) с учетом ответа, О(1) без учета хранения ответа
input = [13, 12, 15, 11, 9, 12, 16]
output = [2, 1, 4, 2, 1, 1, 0]
Вариант 2
Работа со стеком. Уменьшает время работы

"""

temp_list = [13, 12, 15, 11, 9, 12, 16]


def get_next_good_day_1(temp_list):
    result = []
    for i in range(len(temp_list)):
        temp_today = temp_list[i]
        count = 0
        for next_day in temp_list[i+1:]:
            if next_day < temp_today:
                count += 1
            else:
                count += 1
                result.append(count)
                break
    result.append(0)
    return result

def get_next_good_day_2(temp_list):
    result = [0]
    temp_stack = [(temp_list[-1], len(temp_list))]
    for day in temp_list[:(len(temp_list)-1):-1]:
        # todo https://www.youtube.com/watch?v=-59FbGWsCgI&ab_channel=%D0%A1%D0%B0%D1%88%D0%B0%D0%9B%D1%83%D0%BA%D0%B8%D0%BD
        pass




print(get_next_good_day_1(temp_list))
