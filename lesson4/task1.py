import func
try:
    while 1:
        x = int(input("Введите число от 1 до 9: "))
        func.func1(x)
        print(func.func2(x))
        func.func3(x)
        func.func4(x)
except ValueError:
    print('Что-то пошло не так!!!')