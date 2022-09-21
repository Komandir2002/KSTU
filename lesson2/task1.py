s = input('Введите текст')
s = s.split()
print(max(s, key=len))