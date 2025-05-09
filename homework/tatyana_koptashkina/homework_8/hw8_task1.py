import random

salary = int(input())
bonus = random.choice([True, False])

if bonus:
    salary += random.randint(1, 5000)
    print(f"${salary}")
else:
    print(f"${salary}")
