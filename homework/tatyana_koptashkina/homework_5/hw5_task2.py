line1 = "результат операции: 42"
line2 = "результат операции: 514"
line3 = "результат работы программы: 9"

colon1_index = line1.index(':')
number1 = int(line1[colon1_index + 2:])
print(number1 + 10)

colon2_index = line2.index(':')
number2 = int(line2[colon2_index + 2:])
print(number2 + 10)

colon3_index = line3.index(':')
number3 = int(line3[colon3_index + 2:])
print(number3 + 10)
