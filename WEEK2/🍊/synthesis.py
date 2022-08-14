# 1078 _ 공통문제
num = int(input());
sum = 0;
for i in range(1, num):
    if(i % 2 == 0):
        sum += i;
print(sum);