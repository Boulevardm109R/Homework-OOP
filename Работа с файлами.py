import os
from pprint import pprint
#Задача №1

with open('Блюда.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredient_quantity = int(file.readline())
        ingredients_list = []
        for i in range(ingredient_quantity):
            rt = file.readline()
            ingredient_name, quantity, measure = rt.strip().split(' | ')
            employee = {
                'ingridient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients_list.append(employee)
        file.readline()
        cook_book[f'{dish}'] = ingredients_list


#Задача № 2

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingridient_name'] in result:
                    result[consist['ingridient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingridient_name']] = {'measure': consist['measure'], 'quantity': int(consist['quantity']) * (person_count)}
        else:
            print('Такого блюда нет в книге')
    pprint(result)


get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])


# Задача №3
def write_file():
    files = os.listdir('.')
    files = [file for file in files if file.endswith('1.txt') or file.endswith('2.txt') or file.endswith('3.txt')]
    files_info = {}
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            files_info[file] = {
                'num_lines': len(lines),
                'content': lines
            }
            files_sorted = sorted(files_info.items(), key=lambda x: x[1]['num_lines'])
            with open('result.txt', 'w', encoding='utf-8') as f:
                for file_info in files_sorted:
                    file_name = file_info[0]
                    num_lines = file_info[1]['num_lines']
                    f.write(file_name + '\n')
                    f.write(str(num_lines) + '\n')


write_file()
