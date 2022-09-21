def data1(number: int):
    if 0 < number <= 31:
        return f'Месяц:Январь\nДень:{number}'
    elif 31 < number <= 60:
        return f'Месяц:Февраль\nДень:{number - 30}'
    elif 60 < number <= 91:
        return f'Месяц:Март\nДень:{number - 60}'
    elif 91 < number <= 121:
        return f'Месяц:Апрель\nДень:{number - 90}'
    elif 121 < number <= 152:
        return f'Месяц:Май\nДень:{number - 120}'
    elif 152 < number <= 182:
        return f'Месяц:Июнь\nДень:{number - 150}'
    elif 182 < number <= 212:
        return f'Месяц:Июль\nДень:{number - 180}'
    elif 212 < number <= 242:
        return f'Месяц:Август\nДень:{number - 210}'
    elif 242 < number <= 270:
        return f'Месяц:Сентябрь\nДень:{number - 240}'
    elif 270 < number <= 303:
        return f'Месяц:Октябрь\nДень:{number - 270}'
    elif 303 < number <= 334:
        return f'Месяц:Ноябрь\nДень:{number - 300}'
    elif 334 < number <= 365:
        return f'Месяц:Декабрь\nДень:{number - 330}'


print(data1(340))
