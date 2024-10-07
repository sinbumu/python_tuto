#함수
#입력 > 함수 > 출력

#사용자 정의 함수(user-defined functions)와
#내장 함수(built-in functions)로 구분

#함수 머리는 키워드 def

def function1():
    return 1

def hello():
    print("hi python")
    print("hello func end")

print(hello)
hello()

def 인사하기(name,n):
    for x in range(n):
        print("안녕",name)

인사하기('홍길동',3)
인사하기('이순신',2)

#abs(), pow(), round(), divmod(), min(), max(), sum()
# abs(-3)
# pow(2,3)
# round()
# divmod()
# min()
# max()
# sum()

#sorted(), reversed(), all(), any()

#입력값, 리턴값에 따른 함수의 형태
#4가지 패턴 가능
def testSum (a,b):
    c = a+b
    return c

s = testSum(3,4)

#지역(local)변수와 전역(global)변수
#범위(scope)가 다름

#지역 변수는 함수 내부에서 

#전역 변수는 함수 외부에서

#람다 함수
#이름이 없는(익명, anonymous) 함수


#함수 map(function, iterable, ...)
#iterable의 모든 항목에 function을 적용한 후 
# 그 결과를 돌려주는 iterator를 반환

def add(x,y):
    return x+y

arrayA = [10,30,50,20]
arrayB = [1,3,5,2]

lst=list(map(add,arrayA,arrayB))
print(lst)

lst2=list(map(lambda x,y:x+y,arrayA,arrayB))
print(lst2)

##예제 연습들 하는

def getprime():
    return 2,3,4,5
a,b,c,d = getprime()
print(a,b,c,d)

#내장함수 보는듯?
print(abs(-3))
print(pow(2,3))
print(round(3.1415))
print(round(3.1415,3))
print(10//3)
print(10%3)
print(divmod(10,3))
print(min(5,1,10))
print(max(5,1,10))
print(sum([5,1,19]))
print(sum([5,1,19],3))
count=[20,10,80,50]
print(sorted(count))
print(sorted(count, reverse=True))

b=all([3>4, 'p' in 'py'])#전부 true면 true반환
print(b)
print(all(''))

b=any([3>4, 'p' in 'py'])#하나라도 true면 true반환
print(b)
print(any(''))

#함수 최종라인에 return이 아니라 print달면 안된다는걸
#여러번 강조하는데 저럴일이 있나 실무에서????
#에초에 print말고 로깅함수 호출할테고 흠


#람다 연습
lambda x:x+1
lambda x,y:x+y
(lambda x,y:x*y)(10,20)
#print(x) #x는 람다 함수 안에서 로컬로만 존재해서 밖에서 호출 불가



