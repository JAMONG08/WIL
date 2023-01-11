# 겉넓이 구하기 = (전체 겉넓이) - (겹치는 부분의 겉넓이)
# 전체 겉넓이는 중복을 포함한 값이기 때문에 겹치는 부분을 뺴줘야 올바른 값이 나온다

n,m = map(int,input().split())  # 가로, 세로

square = [[0,0,0,0]]  # 도형 담을 배열

for i in range(1, n+1):
  square.append([0]+list(map(int, input().split())))  

# 전체 겉넓이
sum = 0
for i in range(1, n+1):
  for j in range(1, m+1):
    sum += 2 + (square[i][j]*4)  # 2는 한 줄씩 계산할 때 위, 아래의 겉넓이

# 왼쪽 중복 겉넓이
for i in range(1, n+1):
  for j in range(1, m):
    sum -= min(square[i][j], square[i][j+1])*2  # 앞줄, 뒷줄 중 더 작은걸 빼준다 -> 겹치는 부분
                                                # 두 면을 빼줘야 하니 *2

# 앞쪽 중복 겉넓이
for j in range(1, m+1):
  for i in range(1, n):
    sum -= min(square[i][j], square[i+1][j])*2

print(sum)


# 한 면이 구하는 것도 시도했는데 도형 최상단 부분의 겉넓이가 제대로 더해지지 않음
# 참고 : https://earthconquest.tistory.com/308