""" 
숫자 변환하기
문제 설명
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

제한사항
1 ≤ x ≤ y ≤ 1,000,000
1 ≤ n < y
입출력 예
x	y	n	result
10	40	5	2
10	40	30	1
2	5	4	-1
""" 
from collections import deque
def solution(x, y, n):
    if x==y:
        return 0
    #아마 너비 우선 탐색으로 가야 할듯???
    #각 경우를 한턴씩 탐색하면서 불가능 한 애들 탈락. 성공한 경우 시행횟수 save
    #save된 시행횟수보다 높은 애들도 탈락
    #아니다 너비탐색 할꺼면 굳이 비교 필요 없나?
    deq = deque()
    deq.append(x)
    #이거 시간초과 나서...
    #y보다 작은 값들 났을때 기록을 남기고 그거 넘겨야 할듯?
    #아예 카운터 값을 빼버리자 그쪽으로.
    countList = [0 for _ in range(y+1)] #각 value별로 몇회 카운트해서 왔나 기록
    # print(countList)
    while(deq):
        # print(deq)
        z = deq.popleft()
        cvalue = z
        for dir in range(3):
            if dir == 0:
                newValue = cvalue+n 
            if dir == 1:
                newValue = cvalue*2
            if dir == 2:
                newValue = cvalue*3
            if newValue > y or countList[newValue]:
                continue
            if newValue == y:
                return countList[z]+1
            deq.append(newValue)
            countList[newValue] = countList[z]+1
    return -1