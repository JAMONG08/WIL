# 요세푸스 문제 0
'''
from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

q = []
answer = []
for i in range(0, n):
    q.append(False)

i = flag = 0
while q.count(False) > 0:
    if(flag == n):
        flag = 0

    if(q[flag] == True):
        flag += 1
        continue

    if(i == 2):
        q[flag] = True
        answer.append(flag+1)
        i = 0
        continue
    
    i += 1
    flag += 1

print('<'+','.join(list(map(str, answer)))+'>')
'''


n, k = map(int, input().split())

nums = list(range(1, n+1))
index = k-1
answer = []

while True:
    answer.append(nums[index])
    nums = nums[:index] + nums[index+1:]
    if not nums:
        break
    index = (index + k-1) % len(nums)

print('<'+','.join(list(map(str, answer)))+'>')

'''
    참고: https://jjyoung.tistory.com/122
    https://tagilog.tistory.com/1046
'''