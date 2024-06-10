# orderitem_uuid, order_uuid, item_uuid

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from User.User import User

import random
import csv

class OrderItem(User):
    # def create_uuid(self):

    def get_order_uuid(self):   # move to Order
        header = ['order_uuid', 'order_at', 'store_uuid', 'user_uuid']
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/order.csv', 'r') as f:
            rd = csv.reader(f)
            order_uuid_list = []
            for line in rd:
                if line == header:
                    pass
                else:
                    order_uuid_list.append(line[0])
        
        random_order_uuid = random.choice(order_uuid_list)
        
        return random_order_uuid

    def get_item_uuid(self):   # move to Item
        header = ['item_uuid', 'item_type', 'item_name', 'item_price']
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/item.csv', 'r') as f:
            rd = csv.reader(f)
            item_uuid_list = []
            for line in rd:
                if line == header:
                    pass
                else:
                    item_uuid_list.append(line[0])
        item_uuid = random.choice(item_uuid_list)

        return item_uuid
        
    def generate_single_orderitem(self):
        a = self.create_uuid()
        b = self.get_order_uuid()
        c = self.get_item_uuid()
        order_item = f'{a} {b} {c}'

        return print(order_item)
    
    def orderitem_save_as_dictcsv(self):
        x = int(input('How much OrderItem data you need? :'))

        orderitem_list = []
        for _ in range(x):
            orderitme_dict = {
            'orderitem_uuid' : self.create_uuid(),
            'order_uuid' : self.get_order_uuid(),
            'item_uuid' : self.get_item_uuid()
            }
            orderitem_list.append(orderitme_dict)
        
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/orderitem.csv', 'w') as f:
            header = ['orderitem_uuid', 'order_uuid', 'item_uuid']
            wd = csv.DictWriter(f, fieldnames=header)
            wd.writeheader()

            for dict in orderitem_list:
                wd.writerow(dict)

saemi_oi = OrderItem()