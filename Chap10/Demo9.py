def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        res = fib(n-1) + fib(n-2)
        return res


# 斐波那契数列第6位上的数字
print(fib(6))


# 输出这个数列前6位上的数字
for i in range(1, 7):
    print(fib(i))