import sys
input = sys.stdin.readline

# N개의 정수로 이루어진 수열이 있을 때, 
# 크기가 양수인 = 갯수가 이썽야 한다 음수안됨 = 배열안에 값있는 경우 
# 부분수열 중에서 
# 그 수열의 원소를 다 더한 값이 S(0)가 되는 경우의 수를 구하는 프로그램을 작성하시오.
# -7 -3 3 7  
# (-3 3) (-7 7) (-7 -3 3 7) => 전체 탐색 필요 dfs 

n, s = map(int, input().split())
in_arr = list(map(int,input().split()))
cnt = 0
out_arr = []

def dfs(depth, index,total):
    global cnt
    
    if index == total:
        if sum(out_arr) == s:
            cnt += 1
        return #0이되면 
    for i in range(index,n):
        out_arr.append(in_arr[i])
        dfs(depth + 1, i + 1, total)
        out_arr.pop()    
        print('after  ',out_arr)
 
for j in range(1, n + 1):
    dfs(0, 0, j)
    
print(cnt)