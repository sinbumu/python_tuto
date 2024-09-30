# List
'''
특징
자료형 중 하나, 항목의 나열
시퀀스(sequence) 데이터로 순서가 있음
대괄호 [] 를 사용하며 각각의 항목들은 콤마(,)로 구분
'''

#리스트 만들기
subject = [1,2,3,4,5]

#리스트의 인덱싱 , 슬라이스

#인덱싱
#순서가 있는 자료형 인덱싱 가능 - 0 부터 시작

a = [1,2,3,['a','b','c']]

#보기
for item in a:
    print(item)

#슬라이싱
a=[10,20,30,40,50]
print(a[0])
print(a[0:1])
print(a[0:2])
print(a[0:3])
print(a[0:4])
print(a[0:5])
print(a[0:6]) #이게 좀 특이
'''
파이썬에서는 슬라이스(slice) 범위가 리스트의 길이를 벗어나도 
에러가 발생하지 않습니다. 
슬라이스는 범위 내에서 가능한 요소들만 반환하고, 
인덱스를 벗어나면 그저 빈 리스트를 반환합니다.

실제 코딩시엔 len으로 길이 따지고 작업하는 경우가 많으니 
별로 자주 적용될일은 없을듯?
'''
print(a[-1])

#리스트 연산
#덧셈, 반복, 길이 계산

#수정, 삭제

#리스트의 함수들

#append: 요소 하나를 추가
#insert: 특정 인덱스에 요소 추가
#extend: 리스트를 연결하여 확장

c=[10,20,30]
c.append(40)
print(c)
c.append(50)
print(c)

c.insert(1,10) #c[1]에 10넣음
print(c)
d=[100,200,300]
c.extend(d)
print(c)

#리스트 실습
animal=[[
    'lion','ele','tiger'
],'bird','fish']
print(animal)
print(animal[0])
print(animal[0][1])
#
goods=[]
for i in range(3):
    item=input('구입할 품목은?')
    goods.append(item)
    print(goods)
#
pl=['C','C++','Python','Java']
print(pl[0])
print(pl[1])
print()

for i in range(len(pl)):
    print(pl[i])
#
rsp=['가위','바위','보']
for i in range(len(rsp)):
    print(rsp[i], end=' ')
print()
from random import choice
print('컴퓨터의 가위바위보 5개')
for i in range(5):
    print(choice(rsp), i)
#
food=['자장면','짬뽕','우동','울면']
print(food)
food.append('군만두')
print(food)
food[1]='냥짬뽕'
print(food)
food[food.index('우동')]='mandoo'
print(food)


print('script end')