s = input('Введите текст:')
s = s.split('*')
print(min(s, key=len))