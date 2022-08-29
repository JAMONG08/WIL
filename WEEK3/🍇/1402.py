# 거꾸로 출력하기
# 5 : 입력할 개수
# 1 3 5 6 8 : 입력한 순서
# 8 6 5 3 1 : 출력한 순서

cnt = int(input()) # 총 몇 개 입력받을지

arr = list(range(0, cnt)) # 입력숫자

for i in range(0, cnt):  
  arr[i] = int(input())
  
while(cnt>0):           # cnt가 끝까지 안 돌 듯
  cnt = cnt - 1
  print(arr[cnt], end='\t')

  

