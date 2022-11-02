
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
graph = list([] for _ in range(N+1))

# 연결 요소 개수
res = 0

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False] * (N+1)
def DFS(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            DFS(node)


for i in range(1, N+1):
	if not visited[i]:
		DFS(i)
		res += 1

print(res)
