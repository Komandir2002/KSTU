def func1(x):
    if x <= 3 and x >= 0:
        s = input("Введите строку: ")
        n = int(input('Введите количество повтора строки: '))
        for i in range(n):
            print(s)

def func2(x):
    if x <= 6 and x >= 4:
        m = int(input("Введите степень в котрую хотите возвести:"))
        result = x ** m
        return f"Результат x:{x} в степене m:{m}= {result}"
def func3(x):
    if x <= 9 and x >= 7:
        for number in range(10):
            print(x + number)
            num = number + 1

def func4(x):
    if x < 0 and x > 9:
        print('Ошибка ввода')
