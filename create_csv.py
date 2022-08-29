import csv

with open(f'PARSING.csv', 'w', newline='', encoding='utf-8') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(
        ['Дата'] + ['Конкурент'] + ['Ссылка'] + ['Артикул'] + ['Тип'] + ['CCT'] + ['CRI'] + ['Uнoм,В'] + ['Бренд'] + [
            'Цена'] + ['Остаток'] + ['Серия'] + ['Iбин.'] + ['Iмакс'] + ['Фмин'] + ['Фтип'] + ['Фмакс'] + ['Uмин'] + [
            'Uтип'] + ['Uмакс'] + ['Datasheet'])
