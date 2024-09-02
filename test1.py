def fib_series(num):
    fib = [0, 1]
    for i in range(2, num):
        next_value = fib[i-1] + fib[i-2]
        fib.append(next_value)

    print(fib)

num = 10
fib_series(num)