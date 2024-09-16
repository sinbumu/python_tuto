#다음을 참고로 월(month)을 표준 입력으로 입력 받아 계절을 출력하는 프로그램을 작성하시오.

#1. 봄:4,5 월 , 여름: 6,7,8 , 가을: 9,10 , 겨울: 11, 12, 1, 2, 3

Check = True
if Check:
    print('-'*13)

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