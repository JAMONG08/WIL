# 3051. RGB 거리 (Small)

N = int(input())  # 집의 수
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for j in range(1, len(arr)):
  arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]  # Red 
  arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]  # Green 
  arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]  # Blue 

# print(arr[N-1], end=' ')
print(arr[N-1][0], end=' ')
print(arr[N-1][1], end=' ')
print(arr[N-1][2], end=' ')

print(min(arr[N-1][0], arr[N-1][1], arr[N-1][2]), end=' ')