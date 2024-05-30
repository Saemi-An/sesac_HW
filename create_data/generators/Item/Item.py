# item_uuid, item_type, item_name, item_price

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from User.User import User
import random
import csv

class Item(User):
    # def create_uuid(self):

    def read_items(self):
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/generators/Item/item.txt', 'r') as f:
            lines = f.readlines()
            temp_lst = []
            for line in lines:
                temp_lst.append(line.strip())

        double_list_item = []
        for str_item in temp_lst:
            double_list_item.append(str_item.split(','))
        
        return double_list_item

    def get_single_item(self):
        item_uuid = self.create_uuid()
        a = self.read_items()
        b = random.choice(a)
        item_type = b[0]
        item_name = b[1]
        item_price = b[2]
        item_info = f'{item_uuid} {item_type} {item_name} {item_price}'
        
        return item_info

    def generate_items_show(self):
        x = int(input('How much item data you want?: '))
        show = []
        for _ in range(x):
            single_item = self.get_single_item()
            show.append(single_item)

        return show
        
    def itme_save_as_dictcsv(self):
        x = int(input('How much item data you want?: '))

        item_list = []
        for _ in range(x):
            item_data = random.choice(self.read_items())
            item_dict = {
                'item_uuid' : self.create_uuid(),
                'item_type' : item_data[0],
                'item_name' : item_data[1],
                'item_price' : item_data[2]
            }
            item_list.append(item_dict)

        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/item.csv', 'w') as f:
            header = ['item_uuid', 'item_type', 'item_name', 'item_price']
            wd = csv.DictWriter(f, fieldnames=header)
            wd.writeheader()

            for dict in item_list:
                wd.writerow(dict)   # 왜 [{}] 형태만 저장할 수 있지? 왜 그냥 리스트는 적을 수 없찌?!

saemi_i = Item()
