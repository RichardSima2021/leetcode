def fib(n):
    fib_n_1 = 1
    fib_n_2 = 0
    fib_n = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(0, n - 1):
            fib_n = fib_n_1 + fib_n_2
            fib_n_2 = fib_n_1
            fib_n_1 = fib_n

    return fib_n

print(fib(4))
