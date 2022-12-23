"""
Вывести последнюю цифру большого числа Фибоначчи

Дано число 1≤n≤1071≤n≤107, необходимо найти последнюю цифру nn-го числа Фибоначчи.
input: 841645
output: 5
"""


def fib_digit(n):
    fib_and_list = [0, 1, 1]
    if n <= 2:
        return fib_and_list[n]
    for i in range(3, n):
        fib_and_list.append((fib_and_list[i-1] + fib_and_list[i-2])%10)
    return (fib_and_list[n-1]+fib_and_list[n-2])%10


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
