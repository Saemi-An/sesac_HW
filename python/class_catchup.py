# 2024-05-22.역삼각형 별찍기
# user_input = int(input('pls enter: '))

# for i in range(1,user_input+1):
#     print(' ' * (i-1), end='')
#     print('*' * (2 * user_input - i - (i-1)))


# 2024-05-22.구구단 및 구구단 테이블
# for j in range(2,10):
#     for i in range(1,10):
#         print(f'{j} x {i} =', j*i)
#     print('\n')


# 2024-05-22.max() 함수 사용하지 않고 리스트에서 최대값 찾기
# lst_1 = [1, 3, 4, 8, 2, 3, 9]
# lst_2 = [1, 3, 3, 4, 4, 0, 10]   # 중복
# lst_3 = [-1, 3, 3, 4, 4, 0, -9]  # 음수
# lst_4 = [-1, -3, -3, -4, -4, 0, -9]  # 음수

# for i in lst_4:
#     for j in lst_4:
#         if i >= j:
#             pass
#         else: 
#             i = j
# print(i)


# 2024-05-22.팩토리얼 함수 사용하지 않고 입력값을 받아 팩토리얼 계산하기
# user_input = int(input('pls enter: '))
# result = 1

# for i in range(1, user_input+1):
#     result *= i
# print(result)

# print('------')

# import math
# x = math.factorial(6)
# print(x)


# 2024-05-22.입력값 대/소문자 구분 없이 함수 실행시키기
test_dict = [
    {'name' : 'Song',
    'age' : 32,
    'housing' : 'Yes',
    'car' : 'Carnival'},

    {'name' : 'Saemi',
    'age' : 28,
    'housing' : 'No',
    'car' : 'No'},

    {'name' : 'Sun-a',
    'age' : 28,
    'housing' : 'Yes',
    'car' : 'K3'},

    {'name' : 'Kim',
    'age' : 54,
    'housing' : 'Yes',
    'car' : 'Genesis-G70'},

    {'name' : 'Kim',
    'age' : 20,
    'housing' : 'Yes',
    'car' : 'BMW-IX'},
]
        # 'Saemi', 'saemi' - 대소문자 구분 없이 name 입력
        # 'Kim' - 동명이인이 있는 경우 모두 출력
        # 32 - 숫자만 입력한 경우
        # 'Saemi', 54 - 결국 인자 입력 순서에 상관없이, 검색어에 걸리면 해당되는 값들 모두 출력 - 이는 인자값을 받는 경우에 해당하지만, 인자값 안받고 그냥 유저에게서 입력 받는 형식으로 해결 
# 검색어에 하이라이트 ????? 이건 프론트에서 구현해야하는 부분인가?!
        # 'Saemi 20' 스페이스로 구분하여, 해당 검색어에 있는 모든 결과값 출력

def find_person():
    user_input = input('pls enter: ')   # Saemi 32
    search_lst = user_input.split(' ')   # ['Saemi', '32']
    
    answer_list = []

    for i in search_lst:   # i = 'Saemi', '32' <-- str !!!
        i = i[0].upper() + i[1:].lower()   # 사용자가 대문자로 입력했던 소문자로 입력했던 dict 값에 맞춰 형식 변환 후 비교
        for j in test_dict:
            if i == j['name']:
                answer_list.append(j)

            elif i == str(j['age']):
                answer_list.append(j)

            elif i == j['housing']:
                answer_list.append(j)

            elif i == j['car']:
                answer_list.append(j)

            else:
                pass
    return print(answer_list)

find_person()
