#유용한? 모듈
import math

#팩토리얼
a = math.factorial(4)
print(f'math.factorial(4) is {a}')
a = math.factorial(5)
print(f'math.factorial(5) is {a}')

#제곱근의 값을 반환한다.
b = math.sqrt(25)
print(f'math.sqrt(25) is {b}')

#원주율
print(f"math.pi is {math.pi}")

#절대값
print(f'abs(-3) is {abs(-3)}')

#최대, 최소 값
c = [1,2,3,4,5,6,7,8]
print(f'max() is {max(c)}')
print(f'min() is {min(c)}')

#형변환
str = input('실수를 입력하시오:')
print(f'실수 : {str}')
value = float(str)
print(f'value is {value}')

#정렬
sortedArray = sorted([4,3,1,2])
print(f'sortedArray : {sortedArray}')

myList = [4,2,3,5,1]
myList.sort()
print(myList)

#반올림
print(f'round(4.6) : {round(4.6)}')

#타입체크
print(f'type(myList) : {type(myList)}')

a = '123'
print(f'a : {a}')
print(f'type(a) : {type(a)}')

#얕은복사 , 깊은복사
import copy

a = [[1,2],[3,4]]
print(f'a : {a}')
b = copy.copy(a) #얕은 복사
print(f'b : {b}')

a[1].append(5)
print(f'a : {a}')
print(f'b : {b}')

c=copy.deepcopy(a)#깊은 복사
print(f'a[1].append(100)')
a[1].append(100) 
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')

colors=['red','blue','green']
clone=copy.deepcopy(colors)#깊은 복사
print(f'colors : {colors}')
print(f'clone : {clone}')
clone[0] = 'white'
print(f'colors : {colors}')
print(f'clone : {clone}')

#random
import random

print(f'random.randint(1,6) : {random.randint(1,6)}')
print(f'random.random()*100 : {random.random()*100}')
myList=['red','green','blue']
print(f'random.choice(myList) : {random.choice(myList)}')

for i in range(3):
    print(f'random.randrange(1,11,2) : {random.randrange(1,11,2)}')#이렇게 해서
    #1 3 5 7 9 11 중에랜덤 한단건데... 
    #갠적으로 축약되는거보다 복잡함이 큰거 같아서 랜덤풀 만드는거량
    #랜덤 돌리는거 분리할거 같은데 앵간하면

#calendar
import calendar

cal = calendar.month(2024,10)
#year = int(input("몇년도에 태어남"))
#month = int(input("몇월에 태어남"))
print(f'cal is - \n {cal}')

#keyword
import keyword

# name=input("변수 이름을 입력하세요")
# if keyword.iskeyword(name):
#     print(n)

print(keyword.kwlist)

#함수 작성 예?
def is_prime(n):
    for i in range(2,n):
        if n%i == 0 :
            return False
    return True

n = int(input("정수를 2이상 입력하세요"))
print(is_prime(n))
#pythontutor 라는 곳에서 디버깅 하면서 함 보라고 함

#random 이용해서 패스워드 생성
import random
def genPass():
    a='abcdefghijklmnopqrstuvwxyz0123456789'
    password=''
    for i in range(6):
        index=random.randrange(len(a))
        password=password+a[index]
    return password

print(f'genPass() 1 : {genPass()}')
print(f'genPass() 2 : {genPass()}')
print(f'genPass() 3 : {genPass()}')

#greet func
def greet(name, msg = 'dfsdf'):
    return print(name+msg)
#아마 함수 파라미터에 디폴트 값 넣을수 있단거 보여주려고 한듯?

#사칙연산
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

r1=mul(a=20,b=30)
r2=add(10,r1)
print(f'r1 : {r1}')
print(f'r2 : {r2}')
#이건 왜 해본건지 몰?루

#리스트 응용
#강아지 이름 출력
dogNames = []
while True:
    name = input('강아지 이름을 입력하세요(종료시에는 엔터키)\n')
    if name == '' :
        break
    dogNames.append(name)

print("강아지들의 이름")
for name in dogNames:
    print(name,end=" , ")
print(f'\n\n')


#성적의 평균을 구하고, 80점 이상 성적을 받은 학생의 숫자를 계산해서 출력
STUDENTS = 30
scores=[]
scoreSum = 0
print(f'STUDENTS Num : {STUDENTS}')

for i in range(STUDENTS):
    #value = int(input("성적을 입력하시오:\n"))
    value = int(random.randint(0,100)) 
    print(f'index : {i}')
    print(f'value : {value}')
    scores.append(value)
    scoreSum += value

scoreAvg=scoreSum/len(scores)

highScoreStudents=0
for i in range(len(scores)):
    if scores[i]>=80:
        highScoreStudents+=1

print(f'scoreAvg : {scoreAvg}')
print(f'highScoreStudents : {highScoreStudents}')




print(f'\n\n')
print(f'script end...')















