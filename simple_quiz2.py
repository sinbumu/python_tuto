""" 
없는 숫자 더하기

0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
 numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 
 return 하도록 solution 함수를 완성해주세요.


입출력 예
numbers	                result
[1,2,3,4,6,7,8,0]	        14
[5,8,4,0,6,7,9]	            6


""" 

def solution(numbers):
    #구간이 변칙적으로 주면 못쓰는 방법이지만....
    #모든 수의 합을 미리 넣어놓고 차감하면 빠를듯
    answer = 45
    for num in numbers:
        answer -= num
    return answer
