import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
list = {}
for i in range(1, n+1):
    list[i] = []
for i in range(m):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)

cnt = 0
conn = [0]*(n+1)

for i in range(1, n+1):
    if conn[i] == 0:
        q = deque()
        q.append(i)
        cnt += 1
        conn[i] = cnt

        while q:
            me = q.popleft()
            for next in list[me]:
                if conn[next] == 0:
                    q.append(next)
                    conn[next] = cnt

print(max(conn))

