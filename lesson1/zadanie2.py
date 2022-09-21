
def task2(age):
    try:
        if 0 < age <= 7:
            print("~~~Вам в детский сад~~~~")
        elif 7 < age <= 18:
            print("~~~Вам в школу~~~")
        elif 18 < age <= 25:
            print("~~~Вам в профессиональное учебное заведение~~~")
        elif 25 < age <= 60:
            print("~~~Вам на работу~~~")
        elif 60 < age <= 120:
            print("~~~Вам предоставляется выбор~~~")
        else:
            for i in range(5):
                print("Ошибка! Это программа для людей!")
    except ValueError:
        print("Вы где-то допустили ошибку!")
    
# while 1:
#     age = int(input("Если хотите выйти введите: 0\nВведите свой возраст: "))
#     if age == 0:
#         break
#     task2(age)
    



