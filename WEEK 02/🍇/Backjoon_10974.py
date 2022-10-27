from multiprocessing.dummy import Array
from unittest import result
# 1 2 3 
# 2 1 3
# 3 1 2
# 
# 1 3 2
# 2 3 1
# 3 2 1

def swap(n, m, t, array):   # 중복 여부 확인 조건 추가해보기
  tmp = arr[j]
  arr[j] = arr[i]
  arr[i] = tmp
  
  return arr

num = int(input())

arr = list(range(1, num+1))
# print(arr, end="")

# print(arr[0], end="")

# print(*arr, end='') # 대괄호 해제해서 출력

tmp = 0
for i in range(0, num):
  print(str(arr[i]) + ' ', end="")
  for j in range(0, num):
      if(i != j):
        print(str(arr[j]) + ' ', end="")
        arr = swap(i, j, tmp, arr)
      else:
        arr = swap(i, j, tmp, arr)
        
  print('')  

  


