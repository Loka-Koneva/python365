"""
Дана - скобочная последовательность.
Необходимо ответить, правильная ли она.
"""

test_str = '(()))()))(()))'
test_str_true = '((()()))'

def correct_bracket_sequence(test_str):
    balance = 0
    for bracket in test_str:
        if bracket == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False

    return True

# print(correct_bracket_sequence(test_str_true))

"""
Дана строка из скобок и букв в нижнем регистре. 
Необходимо удалить из нее незакрытые скобки.
"""

test_data = "lee(t(c)o)de)"  # output "lee(t(c)o)de" or "lee(t(co)de)" or "lee(t(c)ode)"
test_data2 = "))(("  # '' or ' '
test_data3 = "a)b(c)d"  # "ab(c)d"


def remove_unnecessary_brackets(test_data):
    balance = 0
    true_list = []
    for i in test_data:
        if i.isalpha():
            true_list.append(i)
            continue
        if i == "(":
            balance += 1
            true_list.append(i)
        if i == ")" and balance-1 >= 0:
            balance -= 1
            true_list.append(i)

    if balance > 0:
        while balance > 0:
            true_list.remove("(")
            balance -= 1

    return ''.join(true_list)

# print(remove_unnecessary_brackets(test_data2))

"""
Определить, является ли последовательность из 3 видов скобок правильной
"""

s1 = "()[]{}"
s2 = "(()}"
s3 = "}(){"

def diff_brackets_sequence(test_str):
    stack = []
    brackets_dict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for bracket in test_str:
        if bracket in brackets_dict.keys():
            stack.append(bracket)
        else:
            bracket_from_stack = stack.pop() if len(stack) > 0 else None
            if bracket != brackets_dict.get(bracket_from_stack):
                return False
    if len(stack) != 0:
        return False
    return True

print(diff_brackets_sequence(s3))
