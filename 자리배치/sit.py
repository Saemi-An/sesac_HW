# (Monitor)
# csv에 저장해서 중복 피할 수 있도록

import time
# S10   S1
# S9    S2
# S7    S4
# S6    S5   (Door)

stu_list = ['이태욱','안새미','박수형','윤석인','김승은','김민서','이효림','정여원','김민희','황조현']
sit_num = [1,2,3,4,5,6,7,8,9,10]
W_2 = {}

import random

for i in range(1, 11):
    x = random.choice(stu_list)
    y = random.choice(sit_num)
    
    stu_list.remove(x)
    sit_num.remove(y)
    
    W_2 = {x:y}
    time.sleep(1)
    print(W_2)


# 리스트에서 값을 지우지 않더라도 중복없이 이름과 숫자를 뽑는 방법 ?
# i 루프가 돌아갈 때마다 딕셔너리에 결과값이 추가되어 최종적으로는 10개의 키와 값이 한번에 나올 수 있도록 ?