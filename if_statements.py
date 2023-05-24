#if 문
#https://wikidocs.net/57

#특이사항 > else if 를 elif 라고 표현함

#PRACTICE
a = int(input('얼마를 가지고 있나 입력'))
b = 30000
if a>=b:
    print('TAXI TIME')
else:
    print('Walk')

#for - in 문
#for [value] in [iterable object] 

#index 를 꺼내서 쓰는 for문 예
a = [1,2,3,4]
for index in range(len(a)):
    print(f'index is {index} and element is {a[index]}')

