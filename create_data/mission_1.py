# 이름, 성별, 나이, 생년월일, 주소 랜덤 생성

import random

class DataGenerator1:
    def create_name(self):
        first_name = ['김', '이', '박', '최', '정', '안', '조', '윤', '장', '임']
        middle_name = ['민', '서', '도', '예', '시', '하', '지', '송', '새', '건']
        last_name = ['준', '윤', '우', '호', '원', '후', '현', '서', '진', '재']
        name = random.choice(first_name) + random.choice(middle_name) + random.choice(last_name)

        return name

    def create_gender(self):
        gender_lst = ['남', '여']
        gender = random.choice(gender_lst)

        return gender 
            
    def create_birthdate(self):
        year = str(random.randint(1980, 2023))
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

        return age_birthdate_lst

    def create_address(self):
        si_lst = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
        gu_lst = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
        street_lst = ['덕릉로', '아리수길', '인수봉로', '오현로', '솔매로', '삼양로', '동남로', '구천면로', '천중로', '통일로', '가좌로', '거북골로', '세검정로', '명지길', '백련사길', '연희로', '증가로', '포방터', '홍지문길', '용마산로', '중랑천로', '봉우재로', '사가정로', '겸재로', '천중로', '진황대로']

        si = random.choice(si_lst)
        gu = random.choice(gu_lst)
        street = random.choice(street_lst)
        street_num1 = str(random.randint(1, 99))
        street_num2 = str(random.randint(1, 99))
        address = f'{si} {gu} {street}{street_num1}길 {street_num2}'

        return address
    
    def misstion_1(self):
        a = self.create_name()   # str
        b = self.create_gender()   # str
        c = self.create_birthdate()   # list - ['16', '2008-02-14']
        d = self.create_address()   # str
        data = a + ',' + c[1] + ',' + b + ',' + c[0] + ',' + d
        return print(data)
    
saemi = DataGenerator1()
saemi.misstion_1()
