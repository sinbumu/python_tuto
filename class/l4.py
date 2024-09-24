#반복문 - for 문

#for var in range(start, end, inc)
#for var in range(repeate)

for v in range(1,3,1):
    print("for loop default")
print('------')

for n in range(1,6,1):
    print(f'for loop default num {n}')
print('------')

for n in range(6):
    print(f'for loop default num {n}')
print('------')

for i in 1,2,3:
    print('login')
    print(f'my character id is {i}')
    print('game start')
    print('exit game')
print('------')

# 수의 나열에서 합과 평균 구하기
a = [1.1,2.5,3.6,4.2,5.4]
sum = 0
for i in a:
    sum += i
    print(i, sum)
else:
    print(f'합: {sum}, 평균: {sum/5}')

#예제로 커피 주문 반복문으로 받기 함

#예제로 지정된 최소 한 자릿수가 포함된 두 자리 정수 찾기

n = input('10진수의 한 자릿수 입력 >>')
print('두 자릿수 정수에서 최소 한 자리수가 %s인 정수 찾기: '%n)
print('결과 '.center(50,'='))

for i in range(10,100):
    snum = str(i)
    if n in snum:
        print(i, end='')

#while 문

'''
기본 형식
while(조건):
    수행할 문장1
    수행할 문장...
'''

n=1
while n<5:
    print('hi')
    n+=1
print('----------')

#구구단... 
gugu = input('10진수의 한 자릿수 입력 >>')
guguNum = int(gugu)
n=1
print(f"구구단 {gugu}단")
while n<=9:
    print(f'{n} x {gugu} = {n*guguNum}')
    n+=1
print('----------')

# 이후 for while 연습영상이....
# 근데 굳이 다 따라하면서 연습할 필요 있나? 애매맨





