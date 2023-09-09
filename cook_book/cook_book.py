with open('recipes.txt') as f:
    seq = f.readlines()

# Приводим строки в порядок, удаляя непечатаемые символы и пустые строки
items = []
for s in seq:
    if s != '\n':
        items.append(s.strip())

cook_book = {}
qty_position = 1

for item in items:
    if item.isdigit():
        dish = []
        ingredients = []

        # Определяем, где название блюда, а где ингредиенты для него
        dish.append(items[qty_position - 1])
        ingr_list = items[qty_position + 1:qty_position + int(item) + 1]

        for ingr in ingr_list:
            ingredient = ingr.split(' | ')
            ingr_dict = {
                'ingredient_name': ingredient[0],
                'quantity': int(ingredient[1]),
                'measure': ingredient[2]
            }
            ingredients.append(ingr_dict)

        dish.append(ingredients)
        cook_book.update([dish])

        qty_position += int(item) + 2


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingred_list = []

    for some_dish in dishes:
        ingreds = cook_book.get(some_dish)

        for ingred in ingreds:
            ingred_name = ingred['ingredient_name']
            ingred_list.append(ingred_name)
            ingred.pop('ingredient_name')

            # Умножаем кол-во ингредиентов на кол-во персон и сортируем,
            # как в примере задания, но непонятно зачем эта сортировка :)
            ingred['quantity'] *= person_count
            sorted_ingred = dict(sorted(ingred.items()))
            ingred_list.append(sorted_ingred)

            # Проверяем ингредиенты на повтор и увеличиваем их кол-во,
            # если они повторяются
            if ingred_list[0] in shop_list.keys():
                ingred_list[1]['quantity'] += \
                    shop_list[ingred_list[0]]['quantity']

            shop_list.update([ingred_list])
            ingred_list = []

    # Непонятно, надо было вернуть список покупок или просто вывести его,
    # поэтому я просто вывел
    print(shop_list)
