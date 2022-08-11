# 1071_20220811
num = input()
len = len(num)
flag = '-1'

while flag != '0':
    flag = num.find(' ') + 1
    n1 = num[0:flag].strip()
    num = num[flag:len]
    if n1 == '0':
        flag = '0'
    else:
        if n1 != '':
            print(n1)
        else:
            print(num)
