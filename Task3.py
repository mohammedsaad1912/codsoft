import random

valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
while True:
    if len == 0:
        break
    len = int(input("Enter the length of password you want: "))
    password = "".join(random.sample(valid_char, len))
    print(f"Password is : {password}")