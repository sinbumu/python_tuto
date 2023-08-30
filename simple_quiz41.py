""" 
3진법 뒤집기
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
입출력 예
n	result
45	7
125	229
""" 
def solution(n):
    coNum = nBaseConvert(n, 3)
    strNum = ''
    for char in str(coNum):
        strNum = char+strNum
    return int(strNum, 3)

def nBaseConvert(n, q):#n : 원래 수 , q : 변환하려는 q진법
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]