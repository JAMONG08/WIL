## BFS (너비우선탐색)

그래프는 정점(vertex, node), 간선(edge)로 이루어진 자료구조

1) 정의
BFS는 시작점에서 인접한 정점을 모두 방문하고, 인접한 정점들에 대해서도 인점한 또 다른 정점을 방문하는 방법

BFS는 모든 정점과 간선을 방문하는 완전탐색

2) 최단 경로
BFS는 간선의 가중치가 모두 1인 그래프에서 최단 경로를 찾기

3) 인접 정점 방문
인접 정점을 방문하기 위해서 자료구조 큐를 사용
1. 현재 정점과 인접한 모든 정점을 큐에 넣고, 다 넣으면 큐 앞에서 새로운 정점을 꺼내서 인접한 정점을 큐에 넣는 작업.
2. 시작점과 연결된 모든 정점을 넣을 때 까지.
- 시작점도 방문 체크
- 큐에서 빼낼때 체크


1 push(queue,start) 
- 시작점 어디서부터 뻗어나갈 것인가?

2 while(notEmpty(Queue)) 종료조건문
3	Node <- pop(queue) 원본찾기
4 if(Node == Goal) 		원본찾기
5	return Node  원하는 알고리즘
6 forall child <- expand(Node)	복사 증가문  
7	push(queue,child) 




from collections import deque

visited = [False] * 10

def bfs(v):
    q = deque([v])
    visited[v] = True
    
    while q: # 큐가 비지 않는 동안
        a = q.popleft()
        print(a,end=' ')

        w = sorted(graph[a]) # 번호가 작은 곳부터 순서대로 방문하기 위해 정렬
        for i in w:
            if not visited[i]:
                q.append(i) # 방문할 곳 append
                visited[i] = True # 방문한 곳 check

-----------------------------

bfs 최단 거리를 구할때 짱

인접 리스트 - 링크드 리스트 사용해서 구현
인접 행렬 - 2차원 배열 사용해서 구현

1) 시간 복잡도
인접 리스트 - 시간 복잡도는 O(V+E)
(V는 정점의 수, E는 간선의 수)

인접 행렬 - 시간 복잡도는 O(v^2)
(V는 정점의 수)

6) 경로 추적
DFS // BFS - 가중치가 없(거리1) 그래프 둘 다 완전탐색 bfs -> 레벨별로 탐색을  최단거리, 또는 최소횟수 + 그래프를 사용한다 BFS

DFS 
BFS 일정한 경우의수를 구하는건 같은데 = 구하는 조건 - 아무튼 완전탐색
DP 월급 - 며칠뒤면 +n만원 하고 - 재귀 = 구하는 조건이 재귀

어떤 경우의 수를 구한다거나 하면 DFS를 사용하고, 최단거리, 또는 최소횟수