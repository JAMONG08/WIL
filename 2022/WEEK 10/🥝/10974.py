'''
모든 순열

알고리즘 DFS

그래프
정점, 간선

참고 : 리스트 요소 한번에 출력 https://yeomss.tistory.com/160 

'''
n = int(input())
visited = [False] * (n+1)
s = []

# 깊이 우선 탐색
def dfs():
  # print("dfs", len(s))
  if len(s)==n :
    print(*s) # 참고
    return
  
  for i in range(1, n+1):
    if visited[i] == False:
      s.append(i)
      visited[i] = True
      dfs()
      s.pop()
      visited[i] = False

dfs()
