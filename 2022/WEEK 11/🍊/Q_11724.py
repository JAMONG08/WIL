# 연결 요소의 개수

from collections import deque

import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arr = [[0 for j in range(n+1)] for i in range(n+1)]
stack = visited = deque()
count = 0

for i in range(0, m):
    t1, t2 = map(int, input().split())
    arr[t1][t2] = arr[t2][t1] = 1


def DFS(s):
    global arr, stack

    stack.append(s)

    for i in range(len(arr[s])):
        if arr[s][i] == 1 and i not in stack:
            DFS(i)


for j in range(1, n+1):
    if j not in stack:
        DFS(j)
        count += 1

print(count)




'''
    https://ji-gwang.tistory.com/292
    https://velog.io/@devjuun_s/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%EB%B0%B1%EC%A4%80-11724%EB%B2%88python
'''