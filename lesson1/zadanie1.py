try:
    while 1:
        x = int(input("Введите число от 1 до 9: "))
        if x <= 3 and x >= 0:
            s = input("Введите строку: ")
            n = int(input('Введите количество повтора строки: '))
            for i in range(n):
                print(s)
        elif x <= 6 and x >= 4:
            m = int(input("Введите степень в котрую хотите возвести:"))
            result = x ** m
            print(f"Результат x:{x} в степене m:{m}= {result}")

        elif x <= 9 and x >= 7:
            for number in range(10):
                print(x + number)
                num = number + 1
        else:
            print('Ошибка ввода')

except ValueError:
    print('Вы ввели неправильные данные')
