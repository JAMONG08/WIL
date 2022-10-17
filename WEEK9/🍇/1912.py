import sys

n = int(input())
plus = list(map(int, sys.stdin.readline().split()))
sum = [plus[0]] # 처음에 비교하기 위한 기준값

for i in range(n-1):
  # print(sum[i]+plus[i+1], ' ', plus[i+1], ' ')
  # print(plus[i+1])
  sum.append(max(sum[i]+plus[i+1], plus[i+1]))  # 기준값+다음값, 다음값 중 큰 값을 sum에 넣음 
                                                # -> 1개 이상 고르는 거니까 안 더해도 됨

print(sum)