# 1087_20220814_개별문제
num = int(input());
sum = 0;
for i in range(1, 100000000):
    sum += i;
    if(sum >= num):
        break;
print(sum);

###############################################
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
'''
cnt = int(input());
nums = input().split();
for i in range(cnt):
    print(nums[i]);
'''

# 1073_20220815
'''
nums = input().split();

for i in range(len(nums)):
    if(nums[i] != '0'):
        print(nums[i]);
    else:
        break;
'''

# 1074_20220816
'''
num = int(input());

for i in range(num, 1, -1):
    print(i);
'''

# 1075_20220816
'''
num = int(input());

for i in range(num, 0, -1):
    print(i);
'''

# 1076_20220817
'''
c = ord(input());
p = '';

for i in range(97, c+1):
    p += chr(i)+' ';
print(p);
'''

# 1077_20220818
'''
num = int(input());

for i in range(0, num+1):
   print(i);
'''