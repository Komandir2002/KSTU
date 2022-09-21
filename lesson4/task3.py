import random

print('~~~Шар предсказания~~~')
answers = ['Да это было хорошо','Мне не понравилось',' Я согласен','Крууто!','Very good','Чувствую себя плохо','Я рад','Ураа','nice!','fany']
while 1:
    question = input('Слушаю ваш вопрос: ')
    ans = random.choice(answers)
    print(f'Вопрос: {question}-{ans}')