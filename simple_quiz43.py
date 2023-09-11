""" 
숫자 짝꿍
문제 설명
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

제한사항
3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
X, Y는 0으로 시작하지 않습니다.
X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.
입출력 예
X	Y	result
"100"	"2345"	"-1"
"100"	"203045"	"0"
"100"	"123450"	"10"
"12321"	"42531"	"321"
"5525"	"1255"	"552"
""" 
def solution(X, Y):
    answer = ''
    # ★ 포인트1. 반복되는 숫자를 저장하기 위한 dictionary (key: 0 ~ 9)
    numx = {str(n):0 for n in range(10)}
    numy = {str(n):0 for n in range(10)}
    
    # X 문자열 하나씩 돌면서 카운트
    for x in X:
        numx[x] += 1
    
    # Y 문자열 하나씩 돌면서 카운트
    for y in Y:
        numy[y] += 1
    
    # ★ 포인트2. 9부터 0까지 반복문 돌기. sort를 안 하기 위함.
    #           짝꿍을 큰 수부터 더해가면 자동으로 제일 큰 수가 됨.
    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(numx[k], numy[k])
        
        # ★ 포인트3. "000" -> "0"으로 만들어주기 위한 조건문
        if answer == '' and k == '0' and iternum != 0:
            return "0"
        
        # 실패 코드 #############################
        # for _ in range(iternum):             #
        #     answer = ''.join([answer, k])    #
        ########################################
        # 성공 코드 ★★★★★
        # '9'*3 = '999'가 되는 원리를 이용
        answer = ''.join([answer, k*iternum])  
        ########################################
    
    if answer == '':
        return "-1"
    else:
        return answer