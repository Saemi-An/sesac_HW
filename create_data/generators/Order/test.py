import random

item_list = [
    ['Coffee', 'Americano', '3000'], ['Coffee', 'Iced_Americano', '3500'], ['Coffee', 'Latte', '4500'], ['Coffee', 'Iced_Latte', '5000'], ['Coffee', 'Cafè_Mocha', '5000'], ['Coffee', 'Iced_Cafè_Mocha', '5500'], ['Coffee', 'Iced_Einspänner', '6000'], ['Non-Coffee', 'Hot_Chocolate', '4000'], ['Non-Coffee', 'Grapefruit_Ade', '5000'], ['Non-Coffee', 'Passionfruit_Ade', '5000'], ['Non-Coffee', 'Green_Tea', '4500'], ['Non-Coffee', 'Chamomile Tea', '4500'], ['Dessert', 'Chocolate_Banana_Cake', '6000'], ['Dessert', 'Strawberry_Cheese_Cake', '7500'], ['Dessert', 'Chocolate_Chip_Cookie', '4500'], ['Dessert', 'Financier', '3200'], ['Dessert', 'Salted_Caramel_Egg_Tart', '4200']
    ]


weights = [0.25, 0.385, 0.16, 0.12, 0.05, 0.02, 0.01, 0.005]
num_lst  = random.choices(range(1, 9), weights)
for i in num_lst:
    num = i

selected_item = []
for _ in range(num):
    x = random.choice(item_list)
    selected_item.append(x)

selected_item = [
    ['Dessert', 'Salted_Caramel_Egg_Tart', '4200'],
    ['Dessert', 'Chocolate_Banana_Cake', '6000'],
    ['Dessert', 'Chocolate_Banana_Cake', '6000'],
    ['Non-Coffee', 'Passionfruit_Ade', '5000'],
    ['Dessert', 'Chocolate_Chip_Cookie', '4500'],
    ['Dessert', 'Salted_Caramel_Egg_Tart', '4200']
    ]

