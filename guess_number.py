import os

secret_number = list([])
answer_count = int(1)

os.system('cls')

def input_number():
    input_value = input('Write secret number : ')
    secret_number.append(input_value)

input_number()

if secret_number[0].strip().isdigit():
    print('ok')
else:
    print('Only numbers please ! ')
    input_number()

os.system('cls')

while answer_count:
    guest_number = input('Try guess the number : ')
    if guest_number > secret_number[0]:
        print('Number too high, try again ')
    elif guest_number < secret_number[0]:
        print('Number too low, try again ')
    elif guest_number == secret_number[0]:
        print('Perfect !!! You tried ',answer_count,' times')
        break
    answer_count += 1