# https://www.acmicpc.net/step/22
# 덩치순서 구하기 (x,y) (p,q)

n = int(input())

data_list = []
rank = []
# 배열 돌아가면서 리스트에 담기 
for i in range(n):
    a, b = map(int, input().split())
    data_list.append((a,b))

for i in range(n):
    cnt = 0
    for j in range(n): 
        if(data_list[i][0] < data_list[j][0] and data_list[i][1] < data_list[j][1]):
            cnt += 1
    rank.append(cnt + 1)
        
print(*rank)

