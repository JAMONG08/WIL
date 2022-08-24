# 거꾸로 출력하기
# 5 : 입력할 개수
# 1 3 5 6 8 : 입력한 순서
# 8 6 5 3 1 : 출력한 순서

cnt = int(input())

arr = list(range(0, cnt))

for i in range(0, cnt):  
  num = int(input())
  arr[i] = num
  
while(cnt>0):
  cnt = cnt - 1
  print(arr[cnt], end='\t')

  

