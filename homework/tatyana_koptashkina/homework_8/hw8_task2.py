def fibonacci():
    a, b = 0, 1
    count = 1
    while True:
        yield a
        a, b = b, a + b
        count += 1


fib_index = 1
for a in fibonacci():
    if fib_index == 6:
        print(a)
    if fib_index == 201:
        print(a)
    if fib_index == 1001:
        print(a)
    if fib_index == 100001:
        print(a)
    fib_index += 1
