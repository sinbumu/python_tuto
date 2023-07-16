""" 
체육복
문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
""" 
def solution(n, lost, reserve):
    #탐욕법으로 접..근?
    #일단 n의 개수가 최대 30이라서 
    #시간복잡도는 좀 널널할지도.
    #일단 단 한명에게만 빌려줄 수 있는걸 먼저 다 줘버리고
    #두명에게 줄 수 있는건 이후에 대충 주면?
    
    tempRemoveLost = []
    tempRemoveReserve = []
    
    #본인 체육복
    for lNum in lost:
        for rNum in reserve:
            if lNum == rNum:
                #저장
                tempRemoveLost.append(lNum)
                tempRemoveReserve.append(rNum)
                break
    
    for num in tempRemoveLost:
        lost.remove(num)
    
    for num in tempRemoveReserve:
        reserve.remove(num)
        
    tempRemoveLost = []
    tempRemoveReserve = []
    
    #1명만 줄 수 있
    for lNum in lost:
        for rNum in reserve:
            if lNum-1 == rNum or lNum+1 == rNum:
                if rNum+1 in lost and rNum -1 in lost:#2명 줄 수 있음 넘겨
                    continue
                #저장
                tempRemoveLost.append(lNum)
                tempRemoveReserve.append(rNum)
                break
    
    for num in tempRemoveLost:
        lost.remove(num)
    
    for num in tempRemoveReserve:
        reserve.remove(num)
    
    #나머지 차감. (lost가 제로면 pass)
    if len(lost) != 0:
        tempRemoveLost = []
        tempRemoveReserve = []
        for lNum in lost:
            for rNum in reserve:
                if lNum-1 == rNum or lNum+1 == rNum:
                    if rNum in tempRemoveReserve:#이미 들어있으면 패스
                        continue
                    #저장
                    tempRemoveLost.append(lNum)
                    tempRemoveReserve.append(rNum)
                    break
        for num in tempRemoveLost:
            lost.remove(num)
    
    return n-len(lost)