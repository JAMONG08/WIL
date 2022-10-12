# 일곱 난쟁이
import sys
input = sys.stdin.readline

n = 9
list = []
for i in range(0, n):
    list.append(int(input()))

list.sort()

sum = sum(list)
for i in range(n):
    if(len(list) != 7):
        for j in range(i+1, n):
            if(sum - list[i] - list[j]) == 100:
                list.remove(list[i])
                list.remove(list[j-1])
                break

print('\n'.join(map(str, list)))

'''
    참고: https://dongdongfather.tistory.com/72
    https://ywtechit.tistory.com/133
'''