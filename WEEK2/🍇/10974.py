from multiprocessing.dummy import Array
from unittest import result


def swap(n, m, t, array):
  tmp = arr[j]
  arr[j] = arr[i]
  arr[i] = tmp
  
  return arr

num = int(input())
arr = list(range(1, num+1))

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

  


