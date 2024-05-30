
# 1 인스턴스 생성 : 왜 import한 모듈이 들어있는 파일에 각기 다른 이름으로 객체를 생성하지 않으면 실행이 안되는지 ???
# 2 메인함수 : 메인함수 쓰는법?
# 1, 2번을 하지 않고 그냥 임포트 해오면 왜 임포트해온 애들이 먼저 실행되는지?

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from generators.User.User import saemi_u
from generators.Store.Store import saemi_s
from generators.Item.Item import saemi_i
from generators.Order.Order import saemi_o
from generators.OrderItem.OrderItem import saemi_oi


def temp():
    x = int(input(
        'Which data do you want to generate?\n'
        '1 User\n'
        '2 Store\n'
        '3 Item\n'
        '4 Order\n'
        '5 OrderItem\n'
        'Please enter number : '
    ))
    if x == 1:
        saemi_u.user_save_as_dictcsv()
    elif x == 2:
        saemi_s.store_save_as_dictcsv()
    elif x == 3:
        saemi_i.itme_save_as_dictcsv()
    elif x == 4:
        saemi_o.order_save_as_dictcsv()
    elif x == 5:
        saemi_oi.orderitem_save_as_dictcsv()
    else:
        print('Error. Please try again.')

temp()