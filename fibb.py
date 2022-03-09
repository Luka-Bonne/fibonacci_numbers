def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        t = b
        b = a + b
        a = t
    return



fib(10)