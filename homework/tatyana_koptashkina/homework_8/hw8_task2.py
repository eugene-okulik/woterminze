def fibonacci(limit=100002):
    a, b = 0, 1
    count = 1
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


fib_index = 1
for a in fibonacci(100002):
    if fib_index == 6:
        print(a)
    if fib_index == 201:
        print(a)
    # if fib_index == 1001:
        # print(a)
    # if fib_index == 100001:
        # print(a)
    fib_index += 1
