#퇴사 
import sys

n = int(sys.stdin.readline())
    
dp = [0 for i in range(n+1)]

for i in range(n):
    T, P = map(int,sys.stdin.readline().split())
    dp[i+1] = max(dp[i],dp[i+1]);
    if(i + T <= n): 
        dp[i+T] = max(dp[i+T],dp[i] + P)
        print(1)
        
    
print(dp[n]) # 45 