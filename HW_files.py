from pprint import pprint
file_name = 'recipes.txt'

def catalog_reader(file_name):
    with open(file_name, encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            ingredients = []
            for item in range(int(file_obj.readline())):
                ingredient = file_obj.readline().strip().split(' | ')
                cook_book_values = {'ingredient_name' : ingredient[0], 'quantity' : int(ingredient[1]), 'measure' : ingredient[2]}
                ingredients.append(cook_book_values)
            cook_book[dish] = ingredients
            file_obj.readline()
        return cook_book

print(catalog_reader(file_name))

print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr_dict in catalog_reader(file_name)[dish]:
            ingredient_name, quantity, measure = ingr_dict.values()
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': (int(quantity) * person_count)}
            else:
                shop_list[ingredient_name]['quantity'] += (int(quantity) * person_count)

    pprint(shop_list)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
