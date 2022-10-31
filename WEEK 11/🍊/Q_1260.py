# DFS와 BFS

from collections import deque


def DFS(s):
    global arr, stack
    
    stack.append(s)
    for i in range(len(arr[s])):
        if arr[s][i] == 1 and i not in stack:
            DFS(i)

# def BFS():


n, m, s = map(int, input().split())
arr = [[0 for j in range(n+1)] for i in range(n+1)]
stack = deque[]

for i in range(0, m):
    t1, t2 = map(int, input().split())
    arr[t1][t2] = 1
    arr[t2][t1] = 1

# print(arr)

DFS(s)
print(*stack)


'''
https://jokerldg.github.io/algorithm/2021/03/22/dfs-bfs.html
https://0422.tistory.com/43
'''