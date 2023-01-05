N = int(input())
sch = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

# for i in range(N):
#   sch.append(list(map(int, input().split(' '))))

for i in range(N):
  for j in range(i + sch[i][0], N + 1):  
    if dp[j] < dp[i] + sch[i][1]:
      dp[j] = dp[i] + sch[i][1]

print(dp[-1])
