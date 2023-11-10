import math


while True:
    try:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")

        choice = input()

        if choice == '1':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 + num2
            print("Результат: ", result)

        elif choice == '2':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 - num2
            print("Результат: ", result)

        elif choice == '3':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 * num2
            print("Результат: ", result)

        elif choice == '4':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if num2 == 0:
                result = "Ошибка: деление на ноль"
            else:
                result = num1 / num2
            print("Результат: ", result)

        elif choice == '5':
            num1 = float(input("Введите число: "))
            power = float(input("Введите степень: "))
            result = math.pow(num1, power)
            print("Результат: ", result)

        elif choice == '6':
            num1 = float(input("Введите число: "))
            if num1 < 0:
                result = "Ошибка: квадратный корень из отрицательного числа"
            else:
                result = math.sqrt(num1)
            print("Результат: ", result)

        elif choice == '7':
            num1 = int(input("Введите число: "))
            result = 1
            for i in range(2, int(num1) + 1):
                result *= i
            print("Результат: ", result)

        elif choice == '8':
            num1 = float(input("Введите число: "))
            result = math.sin(num1)
            print("Результат: ", result)

        elif choice == '9':
            num1 = float(input("Введите число: "))
            result = math.cos(num1)
            print("Результат: ", result)

        elif choice == '10':
            num1 = float(input("Введите число: "))
            result = math.tan(num1)
            print("Результат: ", result)

        elif choice=='':
            break
        else:
            print("Ошибка: неверный выбор операции")
    except:
        print('Ошибка в операции!')