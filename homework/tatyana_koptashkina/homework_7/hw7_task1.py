required_number = 4
user_number = []

while user_number != required_number:
    user_number = int(input())
    if user_number != required_number:
        print('Попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
