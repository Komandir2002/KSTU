from lesson3 import task2


try:
    while 1:
        x = int(input("Введите число от 1 до 9: "))
        print(task2.tasks1(x))
except ValueError:
    print('Вы ввели неправильные данные')