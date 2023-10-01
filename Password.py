import random
import string

try:
    password_length = int(input("Введите длину пароля: "))
    if password_length <= 0:
        print("Нужно ввести натуральное число")
        exit()
except ValueError:
    print("Нужно ввести натуральное число")
    exit()

password_characters = string.ascii_letters + string.digits
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

password = ''.join(random.choice(password_characters) for _ in range(password_length))

print("Сгенерированный пароль:", password)