#list > 파이썬은 기본적으로 정적인 Array는 없나봄? 자바의 어레이리스트 같은 개념인 리스트로 배열로 할법한 일도 수행하는듯

# https://velog.io/@ayoung0073/python-list 파이썬의 리스트에 대한 글

# TMI : 파이썬에서 문자열, 리스트, 튜플, 사용자 정의 클래스 등은 시퀀스라고 부름

#practice
list_ex1 = ['a','b','c',[1,2,3]]
number = list_ex1[3]
print(number[0]+number[2])

#두 리스트 합치기
# https://codechacha.com/ko/python-join-lists/
a = [1,2,3,4,5]
b = [5,6,7,8,9]
c = a+b
print(c)

#count(value) 특정 원소 개수 새기

#practice 리스트값삭제
a = [1,3,5,7,9,10]
del a[2]
print(a)
b = [1,3,5,7,9,10]
del b[1:5]
print(b)
a = [1,3,5,7,9,10]
a.remove(9)
print(a)

#파이썬 list는 removeAll 내장함수같은게 없다네? 유틸만들어서 쓸듰?
# https://velog.io/@hssarah/Python-list%EC%97%90%EC%84%9C-remove-all-%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
listA = [1,2,3,4,5,6,7,8,8,8,8,8,8]
removedNum = 8
list_removed = [i for i in listA if i != removedNum]
print(list_removed)

#위에 list선언할때 앞에 변수가딸린 포문이 들어가있는데, 이게 파이썬의 문법중 하난듯
#https://redmuffler.tistory.com/452
#리스트 컴프리헨선
#[valueX for valueX in object [conditions...]] 이런식으로 리스트 생성


#리스트의 원소들 갯수 새는 방법들 모음
#https://jsikim1.tistory.com/218

#리스트 insert append extend 등 설명
#https://wikidocs.net/14#_9




