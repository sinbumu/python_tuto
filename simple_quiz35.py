""" 
소수 만들기
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
""" 
import math

def solution(nums):
    #제곱근 까지만 수색하면 된다는 사실을 이용.
    answer = 0
    checkNum = 0
    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if idx1 >= idx2:
                continue
            for idx3, num3 in enumerate(nums):
                if idx2 >= idx3:
                    continue
                checkNum = num1 + num2 + num3
                # print('log')
                # print(idx1)
                # print(idx2)
                # print(idx3)
                # print(checkNum)
                if isPrimeNumber(checkNum):
                    answer += 1
                    
    return answer

def isPrimeNumber(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True