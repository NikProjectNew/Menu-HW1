
from pprint import pprint
with open("recipes.txt", "rt", encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        quatity = int((file.readline().strip()))
        recipes = []
        for _ in range(quatity):
            ingredient, size, measura = file.readline().strip().split(" | ")
            recipes.append({
                'ingredient_name': ingredient,
                'quantity': int(size),
                'measure': measura
            })
        file.readline()
        cook_book[name_dish] = recipes
# pprint(cook_book, sort_dicts = False)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


