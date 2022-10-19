from sys import stdin # sys모듈의 stdin 

n = int(stdin.readline()) # 개수
list = list(map(int, stdin.readline().split())) # n개의 정수
dp = [0] * (n) # idx까지 더한 가장 큰 수

dp[0] = list[0] # 맨 첫번째 값 넣어주기

for i in range(1, n):
  
  # list[i] 값과 dp[i-1] + list[i] 값을 비교하여 더 큰값을 DP[i]에 대입
  # print(i, list[i], dp[i-1])
  dp[i] = max(list[i], dp[i-1] + list[i])
  
print(max(dp))
