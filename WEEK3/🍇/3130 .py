# 모든 소들은 일렬로 서 있고 오른쪽만 볼 수 있다 (뒤의 숫자만 확인)
# N : 순번, H : 키
# 키가 같거나 크면 다음 소들의 헤어스타일을 볼 수 없다
# N=6, H = {10, 3, 7, 4, 12, 2}

num = int(input())  # N

cow = list(num)
tmp = 0         # 비교 변수
sum = 0         # 소들이 확인 수

for i in cow:
  cow[i] = int(input())

for i in cow:
  cnt = 0     # 각각의 소가 본 수
  tmp = cow[i]
  if(tmp > cow[i+1]):
    cnt = cnt+1
  elif(tmp < cow[i+1]):
    cow.pop()
    break

  sum = cnt
    
print(sum)