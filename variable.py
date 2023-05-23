#형변환
# https://wikidocs.net/21059
# >>> float(3)    #실수형으로 바꿈
# 3.0
# >>> int(3.0)    #정수형으로 바꿈
# 3
# >>> str(3)  #문자열로 바꿈
# '3'

#변수명명
#숫자로 시작 안함, 카멜케이스나 스네이크케이스 식으로 명명함
#파이썬은스네이크케이스로 쓰는듯?

#문자 자료형
#직접 선언시 "" '' 등으로 감쌈
x = 'a'
print(ord(x))
t1 = """hello
world"""
print(t1)
t2 = 'hello\nworld'
print(t2)

b = "pytho's is easy"
print(b)

c = "쌍따옴표(\")는 파이썬에서 문자를 의미한다"
print(c)

#문자열 더하기, 곱하기
a = 'python'
b = 'is fun'
c = a + ' ' + b
print(c)

c = a*2 + ' ' + b
print(c)

#index
a = '123456789'
print(a[5])
b = [1,2,3,4,5]
print(b[0])
c = 'python\'s fun'
print(c[3])

d = "python's fun python's fun python's fun"
print(d[-1])

e = 'sadjflasjglirajglkl'
print('str length >> '+str(len(e)))

#문자열의 슬라이싱
#val[x:y]
a = "python is fun"
print(a[0:6])

print(a[6:])

#val[x:y:z] z는 z-1개씩 건너뜀
#ex : 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
b = a[2:7:2]
print(b)

#연습문제(슬라이싱)
#'20220505children's_day' 슬라이싱을 이용해 date 라는 변수에 날짜 day라는 변수에 children's_day를담아 각각 출력
a = '20220505children\'s_day'
date = a[0:8]
day = a[8:]
print(date)
print(day)


#https://brownbears.tistory.com/421
#PYTHON 포멧팅

#%s 문자열 %d 정수 등등 c++ 에서하듯이 %넣어서

#str.format 도 있던데 이건 뒤에 f-string이있는데 굳이? 싶

#f-string 이게 젤 편한듯 파이썬 버전 낮은거아님?

a = 999
b = 'sss'
print(f"test case {a} and {b}")

# a = input('test str')
# b = input('test num')
# print(f'test code {a} and {b}') #위에 퍼센트사인(%) 쓰는 방식에선 문자열인지 정수인지 실수인지등 선언해야 하니 형이 일치해야 하고 이건그런거 없


#practice
# age = input('insert age')
# weight = input('insert weight')
# print(f'my age is {age}, and weight is {weight} kg')




#str 관련 함수

a = 'sivadoggy_gogogogo'
print(a.count('g'))#count
print(a.find('o'))#find first matched index *if not exist, return -1
#upper , lower 대소문자
#str.strip([chars]) 특정 문자 제거 (없으면 공백 제거)
#replace() 문자열 대체

#split([str]) 특정 문자열 기준으로 쪼겜(없으면 공백)  , 문자열.split(sep='구분자', maxsplit=분할횟수) 
# - sep 파라미터
# 해당 파라미터의 기본값은 none이며, 이때 동작은 띄어쓰기, 엔터를 구분자로 하여 문자열을 자릅니다. none일땐 빈문자열은 제거함
 

#practice
# x = float(input('x값을 입력'))
# y=2.5*x**2+3.3*x+6
# print(y)

#practice
word1 = input('word1 : ')
word2 = input('word2 : ')
word3 = input('word3 : ')
w1 = word1[0:1]
w2 = word2[0:1]
w3 = word3[0:1]
print('==================')
print(f'약자 : {w1+w2+w3}')


