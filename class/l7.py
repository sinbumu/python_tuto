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
#추가로 구글 코랩에서 파일 업로드 하는법
'''
1번 방법
-----
Google Colab에서 구글 드라이브에 있는 파일을 Python 스크립트에서 사용하는 방법은 다음 단계에 따라 쉽게 수행할 수 있습니다.

### 1. 구글 드라이브 마운트하기

먼저, Google Colab에 구글 드라이브를 마운트하여 Colab과 드라이브를 연결해야 합니다. 이렇게 하면 구글 드라이브에 저장된 파일을 Colab에서 읽고 쓸 수 있습니다.

```python
from google.colab import drive
drive.mount('/content/drive')
```

위 코드를 실행하면 Google 계정에 로그인하라는 메시지가 나타나며, 로그인 후 승인 코드를 입력하면 드라이브가 Colab에 마운트됩니다. 마운트된 후에는 `/content/drive/MyDrive/` 디렉터리에서 구글 드라이브의 파일에 접근할 수 있습니다.

### 2. 구글 드라이브에서 파일 경로 지정

이제 구글 드라이브에 있는 특정 파일을 Python 스크립트에서 사용할 수 있습니다. 예를 들어, 구글 드라이브의 `MyDrive` 폴더에 있는 `example.txt` 파일을 사용하려면 파일 경로를 정확히 지정해주면 됩니다.

```python
# 파일 경로 설정 (예: MyDrive 폴더에 example.txt 파일이 있다고 가정)
file_path = '/content/drive/MyDrive/example.txt'

# 파일 열기
with open(file_path, 'r') as file:
    content = file.read()

print(content)
```

### 3. 구글 드라이브에 있는 IPYNB 파일 실행하기

만약 구글 드라이브에 저장된 `.ipynb` 파일을 Colab에서 불러와 실행하려면, 해당 파일을 Colab의 "파일" 메뉴에서 직접 열 수 있습니다.

1. Google Colab 상단 메뉴에서 **File > Open notebook**을 클릭합니다.
2. **Google Drive** 탭으로 이동하여 드라이브에 저장된 `.ipynb` 파일을 선택합니다.

혹은 드라이브에 있는 파일 경로를 사용하여 해당 노트북을 파이썬에서 수동으로 실행하거나, 특정 스크립트를 불러와 실행할 수 있습니다.

이 과정을 통해 구글 드라이브에 있는 파일을 Colab 환경에서 자유롭게 읽고 사용할 수 있습니다.
'''

'''
2번 방법
-----
`from google.colab import files`를 사용한 `files.upload()`는 Google Colab에서 **로컬 컴퓨터**로부터 파일을 업로드하는 방법입니다. 이 방법을 통해 Colab 세션으로 파일을 업로드할 수 있지만, 그 파일은 **일시적으로 Colab의 가상 머신**(VM)에 저장됩니다. 즉, 업로드한 파일은 **현재 세션에서만 사용 가능**하며, Colab 세션이 종료되면 해당 파일은 사라집니다.

### `files.upload()`를 사용한 파일 업로드 방법

1. **파일 업로드**:
   ```python
   from google.colab import files
   uploaded = files.upload()
   ```

   이 코드를 실행하면, 로컬 컴퓨터에서 파일을 선택할 수 있는 창이 뜨고, 선택한 파일이 Colab으로 업로드됩니다. 업로드된 파일은 Colab의 가상 머신 내의 **현재 작업 디렉터리** (`/content/`)에 저장됩니다.

2. **업로드된 파일 확인**:
   `uploaded`는 딕셔너리 형태로 파일 이름을 키로 하고, 그 파일의 내용(byte stream)을 값으로 가집니다.
   
   ```python
   for filename in uploaded.keys():
       print(f"Uploaded file: {filename}")
   ```

### 파일이 존재하는 위치

- 파일은 `/content/` 디렉터리에 업로드됩니다. 이 파일은 Colab 세션이 유지되는 동안에만 해당 위치에 존재하게 됩니다.
- 예를 들어, `example.txt`라는 파일을 업로드한 경우, 경로는 `/content/example.txt`가 됩니다.

```python
# 업로드한 파일 읽기 예시
with open('/content/example.txt', 'r') as file:
    content = file.read()

print(content)
```

### `files.upload()`로 올린 파일과 구글 드라이브

- **`files.upload()`로 올린 파일은 구글 드라이브에 자동으로 올라가지는 않습니다.** 
- 해당 파일은 **Colab의 가상 머신**에만 저장되며, 세션이 종료되면 이 파일도 사라집니다.

### 파일을 구글 드라이브에 저장하기

만약 업로드한 파일을 **구글 드라이브에 저장**하고 싶다면, Colab에서 구글 드라이브를 마운트한 후 파일을 구글 드라이브로 이동하거나 복사할 수 있습니다.

1. **구글 드라이브 마운트**:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **업로드한 파일을 구글 드라이브로 저장**:
   ```python
   import shutil
   shutil.move('/content/example.txt', '/content/drive/MyDrive/example.txt')
   ```

이렇게 하면 Colab 세션이 종료되더라도 구글 드라이브에 파일이 저장되어 계속해서 사용할 수 있습니다.

### 정리

- `files.upload()`는 **로컬 컴퓨터에서 Colab 세션**으로 파일을 업로드하는 기능으로, 파일은 **가상 머신**에 일시적으로 저장됩니다.
- 이 파일은 구글 드라이브에 올라가지 않으며, Colab 세션이 종료되면 사라집니다.
- 파일을 유지하려면 **구글 드라이브로 이동**하거나 **저장**해야 합니다.
'''