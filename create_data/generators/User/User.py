# user_uuid, user_name, user_gender, user_age, user_birthdate, user_address

import random
import uuid
import csv

class User:
    def create_uuid(self):
        uuid_v4 = uuid.uuid4()
        
        return uuid_v4

    def create_user_name(self):
        with open('./generators/User/user_name.txt', 'r') as f:   # 상대경로 : ./
            lines = f.readlines()
            name_lst = []
            name = ''
            for line in lines:
                line = line.strip().split(',')
                x = random.choice(line).strip()
                name_lst.append(x)
            for i in name_lst:
                name += i
                
            return print(name)

    def create_user_gender(self):
        gender_lst = ['남', '여']
        gender = random.choice(gender_lst)

        return gender
            
    def create_age_birthdate_list(self):
        year = str(random.randint(1980, 2023))   # str
        month = str(random.randint(1, 12)).zfill(2)   
        day = str(random.randint(1, 28)).zfill(2)   # 개선점: 1960 ~ 2023년 사이의 날짜를 고려해서 몇까지 할 수 있는지??

        # 나이 계산 >> 4자리 빼기로 단축
        if 0 <= int(year[-2:]) <= 23:
            age = 24 - int(year[-2:])
        elif int(year[-2:]) >23:
            age = 100-int(year[-2:])+24

        # 생년월일 출력
        birthdate = f'{year}-{month}-{day}' 
        age_birthdate_lst = [str(age), birthdate]

        return age_birthdate_lst   # ['16', '2008-02-14'] - list


    def create_address(self):
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/generators/User/address.txt', 'r') as f:
            lines = f.readlines()
            raw_si_gu_street = []
            si_gu_street = ''
            for line in lines:
                line = line.strip().split(',')
                x = random.choice(line)
                raw_si_gu_street.append(x)
            for i in raw_si_gu_street:
                i = i.strip()
                si_gu_street += (i+' ')           
        
        si_gu_street = si_gu_street.strip()
        street_num1 = str(random.randint(1, 99))
        street_num2 = str(random.randint(1, 99))
        address = f'{si_gu_street}{street_num1}길 {street_num2}'
        
        return address   # 경남 도봉구 봉우재로5길 50 - str


    def show_user_data(self):
        x = int(input('How much data you want?: '))
        datum = []
        for _ in range(x):
            a_uuid = self.create_uuid()
            b_name = self.create_user_name()
            c_gender = self.create_user_gender()
            d_age_birthdate = self.create_age_birthdate_list()
            e_address = self.create_address()
            data = f'{a_uuid},{b_name},{c_gender},{d_age_birthdate[0]},{d_age_birthdate[1]},{e_address}'
            datum.append(data)   # str

        return print(datum)   # ['str']
    
    def user_save_as_dictcsv(self):
        x = int(input('How much data you want?: '))
        user_list = []
        for _ in range(x):
            user_dict = {
                'user_uuid' : self.create_uuid(),
                'user_name' : self.create_user_name(),
                'user_gender' : self.create_user_gender(),
                'user_age' : self.create_age_birthdate_list()[0],
                'user_birthdate' : self.create_age_birthdate_list()[1],
                'user_address' : self.create_address()
                }
            user_list.append(user_dict)
        
        with open('/Users/jjaemjjaemi/Desktop/src/HW/create_data/user.csv', 'w') as f:
            header = ['user_uuid', 'user_name', 'user_gender', 'user_age', 'user_birthdate', 'user_address']
            wd = csv.DictWriter(f, fieldnames=header)

            wd.writeheader()
            for dict in user_list:
                    wd.writerow(dict)

    def Genderate_User_Data(self):
        x = input('How do you want to print data? (csv / print): ')
        if x == 'csv':
            self.user_save_as_dictcsv()
            print('Data saved. Pls check your .csv file.')

        elif x == 'print':
            self.show_user_data()
        else:
            print('Type Error: Please try again.')


if __name__ == '__main__':
    saemi_u = User()
    saemi_u.create_user_name()



