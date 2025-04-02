import math

a = float(input())
b = float(input())

arithmetic_mean = (a + b) / 2
print(arithmetic_mean)

if a >= 0 and b >= 0:
    geometric_mean = math.sqrt(a * b)
    print(geometric_mean)
else:
    print("Числа должны быть положительными для вычисления ср. геометрического")



