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

#이후엔 구글 코랩에서 작업했음
'''
from google.colab import files
uploaded = files.upload()

#pandas , matplotlib import 하기
import pandas as pd
import matplotlib.pyplot as plt

#csv 파일 읽어오기, 한글 데이터가 있으므로 encoding='cp949' 추가
#이거 구글 드라이브에서 고치면서 utf된듯?
df = pd.read_csv("seoul_tem.csv")

print(df)

#plot 그래프 그리기, 열추출방법 df["열이름"]
plt.plot(df["평균기온(℃)"])
plt.show()

#히스토그램 그리기
plt.hist(df["평균기온(℃)"], bins=10)
plt.show()

low_sum = df['평균최저기온(℃)'].sum()
print(f'평균최저기온 sum : {low_sum}')

#mean 평균
#std 표준편차
#median 중간값
#min 최소값
#amx 최대값

#정렬

#평균기온 오름차순 정렬
print(df.sort_values(by='평균기온(℃)'))

#평균기온 내림차순 정렬
print(df.sort_values(by='평균기온(℃)',ascending=False))
'''