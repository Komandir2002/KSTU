class Zadanie2:
    def __init__(self,age):
        self.age = age


    def task2(self):
        try:
            if 0 < self.age <= 7:
                print("~~~Вам в детский сад~~~~")
            elif 7 < self.age <= 18:
                print("~~~Вам в школу~~~")
            elif 18 < self.age <= 25:
                print("~~~Вам в профессиональное учебное заведение~~~")
            elif 25 < self.age <= 60:
                print("~~~Вам на работу~~~")
            elif 60 < self.age <= 120:
                print("~~~Вам предоставляется выбор~~~")
            else:
                for i in range(5):
                    print("Ошибка! Это программа для людей!")
        except ValueError:
            print("Вы где-то допустили ошибку!")


obj1 = Zadanie2(19)

obj1.task2()