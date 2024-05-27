# 이름 / 주소를 텍스트 파일을 읽어 랜뽑 가능성을 넓히기
# uuid4 적용

import random
import uuid

class DataGenerator2:
    def create_uuid(self):
        uuid_v4 = uuid.uuid4()
        return uuid_v4

    def create_name(self):
        with open('name.txt', 'r') as f:
            lines = f.readlines()
            name_lst = []
            name = ''
            for line in lines:
                line = line.strip().split(',')
                x = random.choice(line).strip()
                name_lst.append(x)
            for i in name_lst:
                name += i
                
            return name

    def create_gender(self):
        gender_lst = ['남', '여']
        gender = random.choice(gender_lst)

        return gender
            
    def create_birthdate(self):
        year = str(random.randint(1980, 2023))   # str
        month = str(random.randint(1, 12)).zfill(2)   
        day = str(random.randint(1, 28)).zfill(2)   # 개선점: 1960 ~ 2023년 사이의 날짜를 고려해서 몇까지 할 수 있는지??

        # 나이 계산
        if 0 <= int(year[-2:]) <= 23:
            age = 24 - int(year[-2:])
        elif int(year[-2:]) >23:
            age = 100-int(year[-2:])+24

        # 생년월일 출력
        birthdate = f'{year}-{month}-{day}' 
        age_birthdate_lst = [str(age), birthdate]

        return age_birthdate_lst   # ['16', '2008-02-14'] - list


    def create_address(self):
        with open('address.txt', 'r') as f:
            lines = f.readlines()
            street1 = []
            street2 = ''
            for line in lines:
                line = line.strip().split(',')
                x = random.choice(line)
                street1.append(x)
            for i in street1:
                i = i.strip()
                street2 += (i+' ')           
        
        street2  = street2.strip()
        street_num1 = str(random.randint(1, 99))
        street_num2 = str(random.randint(1, 99))
        address = f'{street2}{street_num1}길 {street_num2}'
        
        return address   # 경남 도봉구 봉우재로5길 50 - str


    def misstion_2(self):
        a_uuid = self.create_uuid()
        b_name = self.create_name()
        c_gender = self.create_gender()
        d_age_birthdate = self.create_birthdate()
        e_address = self.create_address()

        data = f'{a_uuid}, {b_name}, {c_gender}, {d_age_birthdate[0]}, {d_age_birthdate[1]}, {e_address}'

        return print(data)
    

saemi = DataGenerator2()
saemi.misstion_2()
