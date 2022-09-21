

def reverse_data(day=int(input('Введите день')), month=str(input('Введите месяц').lower())):
    if month == 'январь':
        return day
    elif month == 'февраль':
        return day + 28
    elif month == 'март':
        return day + 60
    elif month == 'апрель':
        return day + 90
    elif month == 'май':
        return day + 120
    elif month == 'июнь':
        return day + 150
    elif month == 'июль':
        return day + 180
    elif month == 'август':
        return day + 210
    elif month == 'сентябрь':
        return day + 241
    elif month == 'октябрь':
        return day + 271
    elif month == 'ноябрь':
        return day + 301
    elif month == 'декабрь':
        return day + 334

print(reverse_data())
