from lesson3 import task2_1
from lesson3 import task3
from lesson3 import task4
from lesson1 import zadanie2


while 1:
    menu = input('~~~~Выберите задачку:1)Задание1\n'
                 '2)Задание2\n3)lesson3_task3\n'
                 '4)lesson3_task4~~~\n Ваш выбор:')
    if menu == "1":
        x = int(input("Если хотите выйти введите: 0\nВведите число от 1 до 9: "))
        if x == 0:
            break
        task2_1.tasks1(x)
    elif menu == "2":
        age = int(input("Если хотите выйти введите: 0\nВведите свой возраст: "))
        if age == 0:
            break
        zadanie2.task2(age)
    elif menu == "3":
        str = input('Введите текст: ')
        task3.findLen(str)
    elif menu == "4":
        p = int(input("Показатель степени: "))
        n = int(input("Предел: "))
        task4.task4(p,n)
    else:
        print('~~~Такой меню нету!!!~~~')
