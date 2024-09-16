#다음을 참고로 월(month)을 표준 입력으로 입력 받아 계절을 출력하는 프로그램을 작성하시오.

#1. 봄:4,5 월 , 여름: 6,7,8 , 가을: 9,10 , 겨울: 11, 12, 1, 2, 3

# Check = True
# if Check:
#     print('-'*13)

# 월을 입력받아 계절을 출력하는 프로그램

# 사용자로부터 월 입력 받기
month = int(input("월을 입력하세요 (1-12): "))

# 계절을 판별하여 출력
if month in [4, 5]:
    print("봄")
elif month in [6, 7, 8]:
    print("여름")
elif month in [9, 10]:
    print("가을")
elif month in [11, 12, 1, 2, 3]:
    print("겨울")
else:
    print("잘못된 입력입니다.")

print('-'*13)
#근로 시급이 12,000원이며, 일주일에 40시간 이상 근무하면 시급의 1.5배의 급여를 준다고 한다.
#일주일 근로 시간을 35~50시간 사이에서 임의의 난수로 정하고, 주급을 계산해 출력하는 프로그램을 작성하시오.
#반복으로 5회의 근로시간에 대해 출력

import random

# 시급 정의
hourly_wage = 12000

# 주급을 계산하는 함수
def calculate_weekly_wage(hours_worked):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        return (40 * hourly_wage) + (overtime_hours * hourly_wage * 1.5)
    else:
        return hours_worked * hourly_wage

# 5회 반복하여 근로시간과 주급 계산
for i in range(5):
    # 35~50 시간 사이의 난수 생성
    hours_worked = random.randint(35, 50)
    
    # 주급 계산
    weekly_wage = calculate_weekly_wage(hours_worked)
    
    # 결과 출력
    print(f"근로 시간: {hours_worked}시간, 주급: {weekly_wage:,}원")

