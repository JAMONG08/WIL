'''
1로 만들기
https://www.acmicpc.net/problem/1463
'''
from sys import stdin
N = int(stdin.readline())  # 정수 (1보다 크거나 같고, 10의 6승보다 작거나 같은 수)

dp = [0] * (N+1) # idx 0은 사용 x
# N 2,3 은 어차피 값 1이니까 미리 세팅 ====> N이 1, 2 넣으면 list 보다 커서 에러남
# dp[2] = dp[3] = 1 

# 2부터 구하면 됨
for i in range(2, N+1):
  dp[i] = dp[i-1] + 1 # 우선 횟수 증가
  
  if(i%2 == 0):
    dp[i] = min(dp[i], dp[i//2]+1)

  if(i%3 == 0):
    dp[i] = min(dp[i], dp[i//3]+1)
  

print(dp[N])
