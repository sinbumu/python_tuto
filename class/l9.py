#Pandas 라이브러리를 이용한 데이터 분석!

#Pandas : 파이썬에서 사용할 수 있는 데이터 처리 및 분석 라이브러리

#시리즈 Series , 데이터프레임 DataFrame , 패널 Panel 3종류의 데이터 구조 사용

import pandas as pd

#1차원 자료구조 Series
#2차원 자료구조 DataFrame
#3차원 자료구조 Panel

#Pandas의 데이터형
#Objects : 문자 또는 문자열 형
#Int64 : 정수형
#Float64 : 실수형

#리스트 만들기
data = [
    ['01','Kim',25],
    ['02','Lim',24],
    ['03','Chang',20],
    ['04','Shin',27],
]

#리스트를 DataFrame으로 변형하여 변수에 저장
df = pd.DataFrame(data, columns=['번호','이름','나이'])

print(df)
print('----------')

#열 추출
print(df['번호'])
print('----------')

print(df[['이름','나이']])
print('----------')

#행 추출 : loc함수 이용
print(df.loc[0])
print('----------')

print(df.loc[[0,2]])
print('----------')

