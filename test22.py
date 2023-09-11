# alist = input("숫자 연속 입력>>").split()
# numlist = list(map(int,alist))
# print("source list :",numlist)
# for index, value in enumerate(numlist):
#     print(f'value is {value}')
#     if value % 2 == 0 :
#         numlist[index] = 0
# print("edited list :",numlist)


# alist = input("숫자 연속 입력>>").split()
# numlist = list(map(int,alist))
# print("source list :",numlist)
# index = 0
# for value in numlist:
#     print(f'value is {value}')
#     if value % 2 == 0 :
#         numlist[index] = 0
#     index += 1
# print("edited list :",numlist)

alist = input("숫자 연속 입력>>").split()
numlist = list(map(int,alist))
print("source list :",numlist)
for index in range(len(numlist)):
    value = numlist[index]
    print(f'value is {value}')
    if value % 2 == 0 :
        numlist[index] = 0
print("edited list :",numlist)