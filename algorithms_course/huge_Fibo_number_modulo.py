"""
Даны целые числа 1≤n≤10^18 и 2≤m≤10^5
необходимо найти остаток от деления n-го числа Фибоначчи на m.

[
	{ "n": "9", "m": 2, "expected": 0 },
	{ "n": "6", "m": 100, "expected": 8 },
	{ "n": "10", "m": 2, "expected": 1 },
	{ "n": "1025", "m": 55, "expected": 5 },
	{ "n": "12589", "m": 369, "expected": 89 },
	{ "n": "1598753", "m": 25897, "expected": 20305 },
	{ "n": "60282445765134413", "m": 2263, "expected": 974 }
]
"""


def fib_mod(n, m):
    if n < 3:
        return 1
    modulo_list = [0, 1, 1]
    fibo2 = 1
    fibo1 = 1
    flag = True
    for i in range(3, n):
        new_fibo = fibo2 + fibo1
        modulo = new_fibo % m
        if modulo == 1 and modulo_list[i-1] == 0:
            flag = False
            break
        else:
            modulo_list.append(modulo)
        fibo1 = fibo2
        fibo2 = new_fibo
    if flag:
        return (fibo2 + fibo1) % m
    residue = n % (len(modulo_list)-1)
    return modulo_list[residue]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()