# 1071_20220811
'''
num = input()
len = len(num)
flag = '-1'

while flag != '0':
    flag = num.find(' ') + 1
    n1 = num[0:flag].strip() # 문자열 자르기
    num = num[flag:len]
    if n1 == '0':
        flag = '0'
    else:
        if n1 != '':
            print(n1)
        else:
            print(num)
'''

# 1072_20220814
cnt = int(input());
nums = input().split();
for i in range(cnt):
    print(nums[i]);
