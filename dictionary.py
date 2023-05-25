#https://wikidocs.net/72

#key , value 형태의 자료형 (다른 언어의 Hash, Map 같은 거)
#표현방식은 json처럼 생김

#딕셔너리 특징
#key 중복 불가
#value는 다른 key에도 중복가능
dic1 = {'이름': '카카', '나이':3, '성별':'여', '메타':{'이름':'카카'}}

print(dic1)
print(dic1['성별'])
print(dic1['메타']['이름'])

#딕셔너리의 확장
dic1 = {"a":1, "b":2, "c":3}
dic2 = {"a":111, "d":4, "f":5}
dic1.update(dic2)
print(dic1)