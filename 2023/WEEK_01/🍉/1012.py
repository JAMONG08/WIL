#가로 M(1 ≤ M ≤ 50) 세로 N(1 ≤ N ≤ 50), 
#배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
#배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
#각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력

# 이중 for 문 n*m
# O(V+E) = 5V = 500*500*5 = 1250000 < 2억

#자료구조
# 그래프 graph[][]
# 방문-> 따로 주는것 대신 2로 체크 
# deque
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 2
    return 1


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)