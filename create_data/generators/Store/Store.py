# store_uuid, store_type, store_name, store_address

# 다른 경로에 있는 모듈 불러오기 - sys 절대경로 지정   ???
# 상속받은 함수 사용을 위해 from User(폴더명).User(파일명) import User(클래스명)   ???

import random
import csv
from User.User import User

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Store(User):
    # def create_uuid(self):
    # def create_address(self):

    def create_store_type_and_name_list(self):
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/generators/Store/store_type_char.txt', 'r') as f:
            lines = f.readlines()
            store_type_char_list = []
            for line in lines:
                line = line.strip().split(',')
                spec = random.choice(line).strip()
                store_type_char_list.append(spec)

        store_type = store_type_char_list[0]
        store_char = store_type_char_list[1]
        num = random.randint(1, 10)
        store_name = f'{store_type} {store_char} {num}호점'
        store_type_and_name_list = [store_type, store_name]
        return store_type_and_name_list   # ['스타벅스', '스타벅스 노키즈 3호점']
        
    def store_save_as_dictcsv(self):
        x = int(input('How much store data you want?: '))
        store_list = []
        for _ in range(x):
            store_dict = {
                'store_uuid' : self.create_uuid(),
                'store_type' : self.create_store_type_and_name_list()[0],
                'store_name' : self.create_store_type_and_name_list()[1],
                'store_address' : self.create_address()
            }
            store_list.append(store_dict)

        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/store.csv', 'w') as f:
            header = ['store_uuid', 'store_type', 'store_name', 'store_address']
            wd = csv.DictWriter(f, fieldnames=header)
            
            wd.writeheader()
            for dict in store_list:
                wd.writerow(dict)

saemi_s = Store()