from pprint import pprint

with open('dz.txt', encoding='UTF-8') as file:
    lines = file.read().split('\n\n')
    cook_book = {}
    for line in lines:
        elements = line.split('\n')
        ingredients = [element.split(' | ') for element in elements if '|' in element]
        cook_book[elements[0]] = []
        for ingredient in ingredients:
            cook_book[elements[0]].append({'ingredient_name': ingredient[0], 'quantity' : int(ingredient[1]), 'measure': ingredient[2]})


    def get_shop_list_by_dishes(dishes: list, person_count: int):
        result = {}
        for dish in dishes:
            if dish in cook_book:
                for consist in cook_book[dish]:
                    if consist['ingredient_name'] in result:
                        result[consist['ingredient_name']['quantity']] += (consist['quantity']  * person_count)
                    else:
                        result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                              'quantity': (consist['quantity'] * person_count)}
            else:
                print('Такого блюда нет в книге')
        return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))





