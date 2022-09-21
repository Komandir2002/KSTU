class Zadanie1:
    def __init__(self,x):
        self.x = x

    def task(self):
        try:
            while 1:
                if self.x <= 3 and self.x  >= 0:
                    s = input("Введите строку: ")
                    n = int(input('Введите количество повтора строки: '))
                    for i in range(n):
                        print(s)
                elif self.x  <= 6 and self.x  >= 4:
                    m = int(input("Введите степень в котрую хотите возвести:"))
                    result = self.x  ** m
                    print(f"Результат x:{self.x } в степене m:{m}= {result}")

                elif self.x  <= 9 and self.x  >= 7:
                    for number in range(10):
                        print(self.x  + number)
                        num = number + 1
                else:
                    print('Ошибка ввода')

        except ValueError:
            print('Вы ввели неправильные данные')



obj = Zadanie1(6)

obj.task()
