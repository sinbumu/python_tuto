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