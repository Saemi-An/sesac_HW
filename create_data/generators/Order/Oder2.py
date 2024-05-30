
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from User.User import User
import time
import random
import csv

class Order(User):
    # def create_uuid(self):
    
    def get_order_at(self):
        now = time.strftime('%Y.%m.%d %H:%M:%S')
        
        return now
    
    def get_user_uuid(self):

        header = ['user_uuid', 'user_name', 'user_gender', 'user_age','user_birthdate', 'user_address']
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/User/user.csv', 'r') as f:
            rd = csv.reader(f)

            user_uuid_list = []
            for line in rd:
                if line == header:
                    pass
                else:
                    user_uuid_list.append(line[0])
        
        random_user_uuid = random.choice(user_uuid_list)

        return random_user_uuid
    
    def get_store_uuid(self):

        header = ['store_uuid', 'store_type', 'store_name', 'store_address']
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/Store/store.csv', 'r') as f:
            rd = csv.reader(f)

            store_uuid_list = []
            for line in rd:
                if line == header:
                    pass
                else:
                    store_uuid_list.append(line[0])

        random_store_uuid = random.choice(store_uuid_list)

        return random_store_uuid

    def create_order(self):
        
        a = self.create_uuid()
        b = self.get_order_at()
        c = self.get_store_uuid()
        d = self.get_user_uuid()
        
        order_data = f'{a} {b} {c} {d}'

        return order_data
    
    def order_save_as_dictcsv(self):
        x = int(input('How much order data you need?: '))
        order_data = []
        for _ in range(x):
            order_dict = {
                'order_uuid' : self.create_uuid(),
                'order_at' : self.get_order_at(),
                'store_uuid' : self.get_store_uuid(),
                'user_uuid' : self.get_user_uuid()
            }
            order_data.append(order_dict)
        
        with open('order.csv', 'w') as f:
            header = ['order_uuid', 'order_at', 'store_uuid', 'user_uuid']
            wd = csv.DictWriter(f, fieldnames=header)
            wd.writeheader()

            for dict in order_data:
                wd.writerow(dict)

# test ------------------------------------------------

    def temp_function(self):
        # x = int(input('How much data you want?: '))

        # self.create_order() # order_uuid / order_at / user / store 

        # 전체 아이템 리스트를 더블리스트로 불러오기 : item_list
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/Item/item.txt') as f:
            rt = f.readlines()
            item_list = []
            for line in rt:
                item_list.append(line.strip().split(','))

        
        

 










saemi = Order()
saemi.temp_function()
