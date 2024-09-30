#문자열

#len() 길이

text = "Hello kaka"
print(len(text))


#실수의 모든 자릿 수 더하기

def sum_of_digits(number):
    # 실수를 문자열로 변환하고 소수점을 제거한 후 숫자만 남김
    number_str = str(number).replace('.', '')
    
    # 각 자릿수를 정수로 변환하여 합산
    digit_sum = sum(int(digit) for digit in number_str)
    
    return digit_sum

# 예시
number = 1685161.156645
result = sum_of_digits(number)
print(f"{number}의 모든 자릿수의 합: {result}")


#count() join()

#find() index()

#split()

#format()