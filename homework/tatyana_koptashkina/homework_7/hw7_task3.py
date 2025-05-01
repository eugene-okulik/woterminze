line1 = "результат операции: 42"
line2 = "результат операции: 514"
line3 = "результат работы программы: 9"


def proc_result(line):
    pos = line.index(':')
    number = int(line[pos + 2:])
    result = number + 10
    print(result)


proc_result(line1)

