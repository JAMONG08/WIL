import sys
input = sys.stdin.readline

n, s = map(int, input().split())
in_arr = list(map(int,input().split()))
cnt = 0
out_arr = []

def dfs(depth, index,total):
    global cnt
    
    if index == total:
        if sum(out_arr) == s:
            cnt += 1
        return

    for i in range(index,n):
        out_arr.append(in_arr[i])
        dfs(depth + 1, i + 1, total)
        out_arr.pop()    
 
for j in range(1, n + 1):
    dfs(0, 0, j)
    
print(cnt)