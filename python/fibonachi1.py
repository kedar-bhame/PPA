def fib(n):
    a = 0
    b = 1

    for i in range(n):
        print("before a = ",a , " b = ",b)
        a, b = b, (a + b)
        # b = a + b    not work
        # a = b
        print("after a = ",a , " b = ",b)

    return a

print(fib(5))