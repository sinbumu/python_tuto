#Dictionary
#사전 이라는 뜻...
#json포멧처럼 키:벨류 구조로 데이터 담음
#java에선 ArrayList<Object>가 비슷하려나?

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "yaer":1964
}#작성 방식도 json포멧을 알면 익숙함

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

thisdict["yaer"] = 2018
print(thisdict)

thisdict.update({"year":2020})
print(thisdict)

x = thisdict.keys()
print(x) #before the change
thisdict["color"] = "white"
print(x) #after the change

car = {
    "brand":"Ford",
    "model": "Mustang",
    "year":1964
}
x = car.values()

print(x) #before the change
car["year"] = 2020
print(x) #after the change

thisdict = {
    "brand":"Ford",
    "electric":False,
    # "model":"Mustang",
    "yaer":1964,
    "colors": ["red","white","blue"]
}

print(thisdict)

#Get the value fo the "model" key:

x = thisdict.get("model")
print(x) #None

x = car.items()

print(x)

car["year"] = 2020

print(x)

###
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "yaer":1964
}

thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "yaer":1964
}
#마지막 아이템 삭제
thisdict.popitem()
print(thisdict)

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "yaer":1964
}
#지정된 키 이름을 가진 항목을 제거합니다.
del thisdict["model"]
print(thisdict)

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "yaer":1964
}
#delete all
thisdict.clear()
print(thisdict)


##실습 - 영어사전 등록 프로그램 만들기

#1. 메모장에 데이터 만들기
#2. animal_eng.txt로 저장하기
#3. 코랩으로 파일 불러오기

#위 파이썬 코드 샘플 기록해둠
#갠적으론json파일로 기록해두면 더 편할거 같은데
#여기선 txt에다 나열하네
#txt example
'''
강아지, dog
고양이, cat
새, bird
코끼리, elephant
'''
#python code
'''
import pandas as pd

dic={ }
fp=open('animal_eng.txt','r’)   # 파일 읽기 r:read
for line in fp.readlines(): # 행을 목록형으로 반환
    x=line.split(',')
    dic[x[0]]=x[1].replace('\n',‘’)   #치환
fp.close()
print(dic)
print(line)

while 1:
    query=input("동물이름을 적으시오(한글)")
    key = query.lower()   #소문자
if key in dic:
    eng=dic.get(key)
    print("{ }는 영어로는 { } 입니다".format(query, eng)) #오타주의
else:
    print("***등록되지 않은 언어입니다"
'''