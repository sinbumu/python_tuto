#실습?
#뭐 새로운거 배운건 없고 이전강에 했던거 응용해서 코딩해보는 그런 시간이었다

#미세먼지 데이터 시각화

#hour : 1시 ~ 10시 문자열 리스트
#pm25: 시간에 따른 초미세먼지 정수형 배열
#pm10: 시간에 따른 미세먼지 정수형 배열

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

hour = ['1h','2h','3h','4h','5h','6h','7h','8h','9h','10h']
pm25 = np.array([34,37,30,27,35,38,43,42,37,14])
pm10 = np.array([46,49,41,40,81,90,53,52,55,51])

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)

for i in range(10):
  if pm25[i] < 15:
    plt.bar(hour[i],pm25[i],color='blue')
  elif 15<=pm25[i]<35:
    plt.bar(hour[i],pm25[i],color='green')
  elif 35<=pm25[i]<75:
    plt.bar(hour[i],pm25[i],color='orange')
  elif pm25[i]>=75:#여길 굳이 조건을 붙이던데 사실 else해도 됨.
    plt.bar(hour[i],pm25[i],color='red')

plt.title('pm2.5 ')

plt.subplot(2,1,2)
for i in range(10):
  if pm10[i] < 30:
    plt.bar(hour[i],pm10[i],color='blue')
  elif 30<=pm10[i]<80:
    plt.bar(hour[i],pm10[i],color='green')
  elif 80<=pm10[i]<150:
    plt.bar(hour[i],pm10[i],color='orange')
  elif pm10[i]>=150:#여길 굳이 조건을 붙이던데 사실 else해도 됨.
    plt.bar(hour[i],pm10[i],color='red')

plt.title('pm1.0 ')
plt.show()

#####

# random 모듈
# 몬테카를로 시뮬레이션 테스트

import random
import matplotlib.pyplot as plt

incircle=0

simcount=int(input('최대 몇번 시뮬레이션 할까요?'))

circle_center=(0,0)
circle_radius=1

c=plt.Circle(circle_center, circle_radius, ec='b', fill=False)

a=plt.axes(xlim=(-1,1), ylim=(-1,1))
a.add_patch(c)
a.set_aspect('equal')

for i in range(simcount):
  x=random.uniform(-1.0, 1.0)
  y=random.uniform(-1.0, 1.0)
  plt.scatter(x,y,s=2)

  dot_value=x*x+y*y
  if dot_value<=1:
    incircle = incircle+1

print(f'Pi= {4*incircle/simcount}')
plt.show()

#####

#미니 프로젝트
#가위 바위 보

from random import choice

madewin={'가위':'보', '바위':'가위', '보':'바위'}

game=['가위#바위#보 게임', '가위','바위','보']

msg = ['비겼습니다','이겼습니다']

msg.append('졌습니닼ㅋ')#append함수 함 써보라고 이리 한듯

print((game[0]+'시작').center(55,'='))

while True:
  try:
    s='0(exit), 1(scissors), 2(rock), 3(paper) - choose one >>'
    num = int(input(s))
  except:
    num=0


  if num==0:
    break;
  if not(1<=num<=3):
    print('입력이 잘못되었습니다. 다시 입력하세요')
    continue;

  player = game[num]
  com = choice(game[1:])

  print(f'당신 : {player} vs 컴퓨터 : {com}')

  if player == com:
    winner = 0
  elif madewin[player] == com:
    winner =1
  else:
    winner =2

  print(msg[winner]+'\n')

print('\n','exit'.center(55,'='))




