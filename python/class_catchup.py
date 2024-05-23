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
# test_dict = [
#     {'name' : 'Song',
#     'age' : 32,
#     'housing' : 'Yes',
#     'car' : 'Carnival'},

#     {'name' : 'Saemi',
#     'age' : 28,
#     'housing' : 'No',
#     'car' : 'No'},

#     {'name' : 'Sun-a',
#     'age' : 28,
#     'housing' : 'Yes',
#     'car' : 'K3'},

#     {'name' : 'Kim',
#     'age' : 54,
#     'housing' : 'Yes',
#     'car' : 'Genesis-G70'},

#     {'name' : 'Kim',
#     'age' : 20,
#     'housing' : 'Yes',
#     'car' : 'BMW-IX'},
# ]
        # 'Saemi', 'saemi' - 대소문자 구분 없이 name 입력
        # 'Kim' - 동명이인이 있는 경우 모두 출력
        # 32 - 숫자만 입력한 경우
        # 'Saemi', 54 - 결국 인자 입력 순서에 상관없이, 검색어에 걸리면 해당되는 값들 모두 출력 - 이는 인자값을 받는 경우에 해당하지만, 인자값 안받고 그냥 유저에게서 입력 받는 형식으로 해결 
# 검색어에 하이라이트 ????? 이건 프론트에서 구현해야하는 부분인가?!
        # 'Saemi 20' 스페이스로 구분하여, 해당 검색어에 있는 모든 결과값 출력

# def find_person():
#     user_input = input('pls enter: ')   # Saemi 32
#     search_lst = user_input.split(' ')   # ['Saemi', '32']
    
#     answer_list = []

#     for i in search_lst:   # i = 'Saemi', '32' <-- str !!!
#         i = i[0].upper() + i[1:].lower()   # 사용자가 대문자로 입력했던 소문자로 입력했던 dict 값에 맞춰 형식 변환 후 비교
#         for j in test_dict:
#             if i == j['name']:
#                 answer_list.append(j)

#             elif i == str(j['age']):
#                 answer_list.append(j)

#             elif i == j['housing']:
#                 answer_list.append(j)

#             elif i == j['car']:
#                 answer_list.append(j)

#             else:
#                 pass
#     return print(answer_list)

# find_person()

# 2024.5.23 - RANDOM.RANDOM() - 랜덤으로 문자열 생성 (영문 대문자 6자리)
import string
import random

letter_set = string.ascii_letters
# big_letter_set = letter_set[26:]   # str
# mission_5 = ''.join(random.sample(big_letter_set, 6))
# # print(mission_5)


# # 2024.5.23 - RANDOM.RANDOM() - 랜덤 초이스에서 가중치를 고려한 랜덤 
# test_lst = ['안새미', '오송경', '김민희', '허숙희', '강감찬']
# weight_lst = []

# for i in range(1, 11):
#     x = random.choices(test_lst, weights=[0.1, 0.7, 0.1, 0.05, 0.05])
#     weight_lst += x

# print(weight_lst)

# pc1 = (weight_lst.count('안새미')) / 10
# pc2 = (weight_lst.count('오송경')) / 10
# pc3 = (weight_lst.count('김민희')) / 10
# pc4 = (weight_lst.count('허숙희')) / 10
# pc5 = (weight_lst.count('강감찬')) / 10

# print(f'0.1 : {pc1}% / 0.7 : {pc2}% / 0.1 : {pc3}% / 0.05 : {pc4}% / 0.05 : {pc5}%')


# 2024.5.23 - RANDOM.RANDOM() - 램덤 비밀번호 생성 (대소문자, 숫자포함 8자리)
small_letter_set = list(letter_set[:26])
big_letter_set = list(letter_set[26:])
number_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol_set = ['@', '*' '!', '#', '$', '-', '%', '&', '(', ')', '+']

q = small_letter_set + big_letter_set + number_set

# alphabet_lst = small_letter_set + big_letter_set

# x = random.sample(alphabet_lst, 4)
# y = random.sample(number_set, 4)

# PW = ''.join(x + y)
# print(PW)


# 2024.5.23 - RANDOM.RANDOM() - 강력한 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개이상 포함하는 8자리)
# 믹스(대1 + 소1 + 숫1 + 랜덤5)
small = list(random.choice(small_letter_set))   # str
big = list(random.choice(big_letter_set))
num = list(random.choice(number_set))
mix_4 = list(random.sample(q, 4))

k = small + big + num + mix_4
# print(''.join(k))

random.shuffle(k)
# print(''.join(k))



# 2024.5.23 - LIST COMPREHENSHION - 문자열의 글자수를 세는 함수
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'egg']
words_length = [len(i) for i in words]
# print(words_length)

# 2024.5.23 - LIST COMPREHENSHION - 문자열 리스트에서 문자열의 길이가 3 이인 단어들만 선택하기
short_words = [i for i in words if len(i) <= 3]
# print(short_words)


# 2024.5.23 - LIST COMPREHENSHION - 중첩 리스트 펼치기
nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [k for i in nested_lst for k in i]
# print(flattened_list)

# 2024.5.23 - LIST COMPREHENSHION - 특정 조건(5보다 큰 것)을 만족하는 요소 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_5 = [i for i in numbers if i > 5]
# print(greater_than_5)

# 2024.5.23 - LIST COMPREHENSHION - 문자열 리스트에서 첫 글자가 모음인 단어들 선택하기
words_2 = ['apple', 'banana', 'cherry', 'Apricot', 'egg']
vowel_starting_words = [i for i in words_2 if i.lower().startswith('a') or i.startswith('e') or i.startswith('i') or i.startswith('o') or i.startswith('u')]
# print(vowel_starting_words)

