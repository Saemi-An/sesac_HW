# 기능
# 1. 겜 > 저장? > 한 파일에 모두 저장 
# 2. 전체 히스토리 보기
# 3. 전체 히스토리에서 최소점수 소유자들 모두 출력

# 개선점
# 1. 게임 끝나면 자동저장 : 결국 파일에 {변수}를 저장해야함. 하지만 피클은 write만 있고 append는 없다. 히스토리 저장 및 열람을 피클로 할 수 있나?
# 2. txt 파일 저장시 \n 입력 없이도 애초에 한번에 한 줄씩 저장하는 함수?

import random
import pickle
import datetime
import csv


class GAME:
    def __init__(self, name):
        self.name = name

    def Up_Down_Game(self):   # 게임실행 > 이번 게임 트라이 횟수 반환
        answer = random.randint(1, 100)
        print(answer)
        count_lst = ['1']
        for i in range(10):
            user_input = int(input('Pls enter(1 ~ 100): '))
            if user_input > answer:
                print('Down')
                count_lst.append('1')

            elif user_input < answer:
                print('Up')
                count_lst.append('1')

            elif user_input == answer:
                print('You won!')
                break
        return len(count_lst)   # int
    
    def Start_Game(self):   # 게임실행 > wanna save? > save as txt
        tries = self.Up_Down_Game()
        now = datetime.datetime.today().strftime('%Y/%m/%d %H:%M')

        x = input('Do you want to save this score?(Y/N): ')
        if x == 'Y':
            y = input(f'Please copy & paste this: {self.name},{now},{tries}  ').strip()
            f = open('test.txt', 'a')
            f.writelines(f'{y}\n')   # 애초에 한 줄에 한번씩 저장하는 방법은 없음?!
            f.close()
        elif x == 'N':
            pass
    
    def Show_Histories(self):
        f = open('test.txt', 'r')
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()

    def Show_Min(self):
        find_min = []
        f = open('test.txt', 'r')
        lines = f.readlines()
        
        for line in lines:
            try:
                line = line.split(',')
                find_min.append(int(line[2][0]))   # txt
            except:   # 스코어 txt파일로 저장시 줄바꿈 때문에 항상 txt파일 맨 마지막에 빈줄이 생성됨. 포문이 이 빈줄을 돌 때 index out of range 에러 발생.
                pass
# ['saemi', '2024/05/26 23:34', '3\n']
        min_num = min(find_min)

        for line in lines:
            try:
                line = line.split(',')
                if int(line[2][0]) == min_num:
                    print(line)
            except:
                pass

        f.close()


saemi = GAME('saemi')
song = GAME('song')

song.Show_Histories()


        

        


