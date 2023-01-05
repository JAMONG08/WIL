#퇴사 
import sys

n = int(sys.stdin.readline())

data = [0 for i in range(n+1)]    
dp = [0 for i in range(n+1)]

for i in  range(n):
  data[i] = int(input())

dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[0] + data[1], data[0] + data[2], data[1]+ data[2])
 
for i in range(3, n):
  dp[i] = max(data[i] + dp[i-2], data[i] + data[i-1] + dp[i-3], dp[i-1])
 
print(max(dp))
