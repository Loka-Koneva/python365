def f():
    dig_first = list(map(int, input().split()))
    dedline_list = list(map(int, input().split()))
    k = dig_first[2]
    xx = dig_first[1]
    dedline_list = dedline_list[:k]

    min_element = min(dedline_list)
    count = 1

    while count < k:
        count += 1
        copy_list = [x for x in dedline_list if x > min_element]
        element = min(copy_list)
        if min_element + xx > element:
            if min_element + xx not in dedline_list:
                dedline_list.append(min_element + xx)
            min_element = element
        else:
            dedline_list.append(min_element + xx)
            min_element = min_element + xx

    print(min_element)

f()

# Резюме: половина тестов прошла. Остальная - "ошибка во время исполнения" или
# "превышен лимит времени" (хотя выводится 2s и 2s)

# Ввод
#
# 5 7 12
# 5 22 17 13 8
#
# Ввод
#
# 6 5 10
# 1 2 3 4 5 6
