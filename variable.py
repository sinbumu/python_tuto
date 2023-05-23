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

