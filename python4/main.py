from login import authorization,signup
import main

while True:
    print('1. Вход')
    print('2. Регистрация')
    action = input()

    try:
        if action == '1':
            authorization().commands()
        elif action == '2':
            signup().commands()
        else:
            print('Действие не найдено')
    except ValueError as ve:
        print(ve)